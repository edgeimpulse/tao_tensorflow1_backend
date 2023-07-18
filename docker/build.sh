#!/usr/bin/env bash

set -eo pipefail

# Run the env setup script so as to set repository root path.
source "../scripts/envsetup.sh"

registry="nvcr.io"
repository="nvidia/tao/tao-toolkit"

tag="5.0.0-tf1.15.5-base"
local_tag="$USER"

# Build parameters.
BUILD_DOCKER="0"
PUSH_DOCKER="0"
FORCE="0"
RUN_DOCKER="0"

# Parse command line.
while [[ $# -gt 0 ]]
    do
    key="$1"

    case $key in
        -b|--build)
        BUILD_DOCKER="1"
        RUN_DOCKER="0"
        shift # past argument
        ;;
        -p|--push)
        PUSH_DOCKER="1"
        shift # past argument
        ;;
        -f|--force)
        FORCE=1
        shift
        ;;
        -r|--run)
        RUN_DOCKER="1"
        BUILD_DOCKER="0"
        shift # past argument
        ;;
        --default)
        BUILD_DOCKER="0"
        RUN_DOCKER="1"
        FORCE="0"
        PUSH_DOCKER="0"
        shift # past argument
        ;;
        *)    # unknown option
        POSITIONAL+=("$1") # save it in an array for later
        shift # past argument
        ;;
    esac
done


if [ $BUILD_DOCKER = "1" ]; then
    echo "Building base docker ..."
    if [ $FORCE = "1" ]; then
        echo "Forcing docker build without cache ..."
        NO_CACHE="--no-cache"
    else
        NO_CACHE=""
    fi

    docker build --pull -f $NV_TAO_TF_TOP/docker/Dockerfile -t $registry/$repository:$local_tag $NO_CACHE \
        --network=host $NV_TAO_TF_TOP/.

    if [ $PUSH_DOCKER = "1" ]; then
        echo "Pusing docker ..."
        docker tag $registry/$repository:$local_tag $registry/$repository:$tag
        docker push $registry/$repository:$tag
        digest=$(docker inspect --format='{{index .RepoDigests 0}}' $registry/$repository:$tag)
        echo -e "\033[1;33mUpdate the digest in the manifest.json file to:\033[0m"
        echo $digest
    else
        echo "Skip pushing docker ..."
    fi

elif [ $RUN_DOCKER = "1" ]; then
    echo "Running docker interatively..."
    docker run --gpus all -v /home/$USER/tlt-experiments:/workspace/tlt-experiments \
                          --net=host \
                          --shm-size=30g \
                          --ulimit memlock=-1 \
                          --ulimit stack=67108864 \
                          --rm -it $registry/$repository:$tag /bin/bash
else
    echo "Usage: ./build.sh [--build] [--push] [--force] [--run] [--default]"
fi

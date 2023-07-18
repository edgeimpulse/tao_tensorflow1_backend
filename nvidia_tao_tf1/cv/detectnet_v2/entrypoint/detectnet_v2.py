# Copyright (c) 2017-2020, NVIDIA CORPORATION. All rights reserved.

"""TLT command line wrapper to invoke CLI scripts."""

import sys
from nvidia_tao_tf1.cv.common.entrypoint.entrypoint import launch_job
import nvidia_tao_tf1.cv.detectnet_v2.scripts


def main():
    """Function to launch the job."""
    launch_job(nvidia_tao_tf1.cv.detectnet_v2.scripts, "detectnet_v2", sys.argv[1:])


if __name__ == "__main__":
    main()

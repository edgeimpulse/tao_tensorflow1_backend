"""FasterRCNN entry point."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from maglev_sdk.docker_container.entrypoint import main

if __name__ == '__main__':
    main('faster_rcnn', 'nvidia_tao_tf1/cv/faster_rcnn/scripts')

"""
--------------
Video fixtures
--------------
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import allure
import enum
import pytest
import xvfbwrapper

from ui_tests import config
from ui_tests.third_party import process_mutex
from ui_tests.third_party import video_recorder


__all__ = [
    'video_capture',
    'virtual_display',
]


class AttachmentType(enum.Enum):
    """Custom attachment type for video."""

    def __init__(self, mime_type, extension):
        self.mime_type = mime_type
        self.extension = extension

    MP4 = ("video/mp4", "mp4")


@pytest.fixture(scope='session')
def virtual_display(request):
    """Session fixture to run test in virtual X server."""
    if not request.config.option.enable_virtual_display:
        return

    _virtual_display = xvfbwrapper.Xvfb(*config.RESOLUTION)
    # workaround for memory leak in Xvfb taken from:
    # http://blog.jeffterrace.com/2012/07/xvfb-memory-leak-workaround.html
    # and disables X access control
    args = ["-noreset", "-ac"]

    _virtual_display.extra_xvfb_args.extend(args)

    with process_mutex.Lock(config.XVFB_LOCK):
        _virtual_display.start()

    request.addfinalizer(_virtual_display.stop)


@pytest.fixture(autouse=True)
def video_capture(request, virtual_display, report_dir):
    """Autouse function fixture to capture video of test."""
    if not request.config.option.enable_video_capture:
        return

    recorder = video_recorder.VideoRecorder(
        os.path.join(report_dir, 'video.mp4'), config.RESOLUTION)
    recorder.start()

    def fin():
        recorder.stop()
        with open(recorder.file_path, 'rb') as video_file:
            allure.attach('video', video_file.read(), AttachmentType.MP4)

    request.addfinalizer(fin)

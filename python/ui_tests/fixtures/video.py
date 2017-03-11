import os

import allure
import enum
import pytest
import xvfbwrapper

from ui_tests import config
from ui_tests.third_party import video_recorder
from ui_tests.third_party import process_mutex


__all__ = [
    'video_capture',
    'virtual_display',
]


class AttachmentType(enum.Enum):

    def __init__(self, mime_type, extension):
        self.mime_type = mime_type
        self.extension = extension

    MP4 = ("video/mp4", "mp4")


@pytest.fixture(scope='session')
def virtual_display(request):
    """Run test in virtual X server if env var is defined."""
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
    """Capture video of test."""
    if not request.config.option.enable_video_capture:
        return

    recorder = video_recorder.VideoRecorder(
        os.path.join(report_dir, 'video.mp4'))
    recorder.start()

    def fin():
        recorder.stop()
        with open(recorder.file_path, 'rb') as video_file:
            allure.attach('video', video_file.read(), AttachmentType.MP4)

    request.addfinalizer(fin)

import os

import allure
import enum
import pytest

from ui_tests.third_party import video_recorder

__all__ = [
    'video_capture',
]


class AttachmentType(enum.Enum):

    def __init__(self, mime_type, extension):
        self.mime_type = mime_type
        self.extension = extension

    MP4 = ("video/mp4", "mp4")


@pytest.fixture(autouse=True)
def video_capture(request, virtual_display, report_dir):
    """Capture video of test."""
    if request.config.option.disable_video_capture:
        return

    recorder = video_recorder.VideoRecorder(
        os.path.join(report_dir, 'video.mp4'))
    recorder.start()

    def fin():
        recorder.stop()
        with open(recorder.file_path, 'rb') as video_file:
            allure.attach('video', video_file.read(), AttachmentType.MP4)

    request.addfinalizer()

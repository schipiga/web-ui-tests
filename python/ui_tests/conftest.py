"""
---------------
Global conftest
---------------
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

from ui_tests.fixtures import *  # noqa F403
from ui_tests.fixtures import __all__  # noqa F401

__all__ += [
    'pytest_addoption'
]


def pytest_addoption(parser):
    """Add options to pytest."""
    parser.addoption("--enable-video-capture", action="store_true",
                     help="Enable video capture")
    parser.addoption("--enable-virtual-display", action="store_true",
                     help="Disable virtual display")
    parser.addoption("--browser", action='store',
                     choices=['chrome', 'firefox'],
                     help="Browser to launch web app")

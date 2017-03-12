"""
------
Config
------
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

UI_TIMEOUT = 5
PAGE_TIMEOUT = 30
APP_URL = 'https://pipedrive.com'
RESOLUTION = 1366, 768

USER_EMAIL = "vasia@example.com"
USER_PASSWD = "a1b42z3a"
USER_NAME = "Vasia"

TEST_REPORTS_DIR = os.environ.get(
    "TEST_REPORTS_DIR",
    os.path.join(os.getcwd(),  # put results to folder where tests are launched
                 "test_reports"))

XVFB_LOCK = '/tmp/cases_xvfb.lock'

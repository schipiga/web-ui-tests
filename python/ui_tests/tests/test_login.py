"""
-----------
Login tests
-----------
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

from ui_tests import config


def test_user_login_successfully(index_steps, signin_steps):
    """**Scenario:** User logs in successfully

    **Setup:**

    #. Launch browser and open application URL.

    **Steps:**

    #. Switch language to English.
    #. Click link "Login" to go to login page.
    #. Log in with credentials.

    **Teardown:**

    #. Close browser.
    """
    index_steps.switch_language("en")
    index_steps.goto_login()
    signin_steps.login(config.USER_EMAIL, config.USER_PASSWD,
                       name=config.USER_NAME)

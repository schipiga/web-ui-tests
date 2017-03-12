"""
-----------------------
Recovery password tests
-----------------------
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


def test_send_recovery_email(index_steps, signin_steps, recovery_steps):
    """**Scenario:** Email to recovery password is sent.

    **Setup:**

    #. Launch browser and open application URL.

    **Steps:**

    #. Switch language to English.
    #. Click link "Login" to go to login page.
    #. Click link "forgot?" to go to recovery password page.
    #. Specified recovered user email and submit form.

    **Teardown:**

    #. Close browser.
    """
    index_steps.switch_language("en")
    index_steps.goto_login()
    signin_steps.goto_recovery()
    recovery_steps.recovery_password(config.USER_EMAIL)


def test_notify_recovery_email_invalid(index_steps,
                                       signin_steps,
                                       recovery_steps):
    """**Scenario:** Error message about nonexistent recovery email is shown.

    **Setup:**

    #. Launch browser and open application URL.

    **Steps:**

    #. Switch language to English.
    #. Click link "Login" to go to login page.
    #. Click link "forgot?" to go to recovery password page.
    #. Submit nonexistent email and check that error message is shown.

    **Teardown:**

    #. Close browser.
    """
    index_steps.switch_language("en")
    index_steps.goto_login()
    signin_steps.goto_recovery()
    recovery_steps.check_recovery_email_nonexistent_notification()

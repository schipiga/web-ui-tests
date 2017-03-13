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


def test_user_login_logout(index_steps,
                           signin_steps,
                           user_account_steps):
    """**Scenario:** User logs in and logs out successfully

    **Setup:**

    #. Launch browser and open application URL.

    **Steps:**

    #. Switch language to English.
    #. Click link "Login" to go to login page.
    #. Log in with credentials.
    #. Log out.

    **Teardown:**

    #. Close browser.
    """
    index_steps.switch_language("en")
    index_steps.goto_login()
    signin_steps.login(config.USER_EMAIL, config.USER_PASSWD,
                       name=config.USER_NAME)
    user_account_steps.logout()


def test_login_reset_after_flush_session(index_steps,
                                         signin_steps,
                                         user_account_steps):
    """**Scenario:** User session is reset after clear cookies.

    **Setup:**

    #. Launch browser and open application URL.

    **Steps:**

    #. Switch language to English.
    #. Click link "Login" to go to login page.
    #. Log in with credentials.
    #. Restart browser and check that user session is reset.

    **Teardown:**

    #. Close browser.
    """
    index_steps.switch_language("en")
    index_steps.goto_login()
    signin_steps.login(config.USER_EMAIL, config.USER_PASSWD,
                       name=config.USER_NAME)
    user_account_steps.flush_session()


def test_login_reset_after_browser_restart(index_steps,
                                           signin_steps,
                                           user_account_steps):
    """**Scenario:** User session is reset after browser restart.

    **Setup:**

    #. Launch browser and open application URL.

    **Steps:**

    #. Switch language to English.
    #. Click link "Login" to go to login page.
    #. Log in with credentials.
    #. Restart browser and check that user session is reset.

    **Teardown:**

    #. Close browser.
    """
    index_steps.switch_language("en")
    index_steps.goto_login()
    signin_steps.login(config.USER_EMAIL, config.USER_PASSWD,
                       name=config.USER_NAME)
    user_account_steps.check_session_reset_after_browser_restart()


def test_login_saved_after_browser_restart(index_steps,
                                           signin_steps,
                                           user_account_steps):
    """**Scenario:** User session is saved after browser restart.

    **Setup:**

    #. Launch browser and open application URL.

    **Steps:**

    #. Switch language to English.
    #. Click link "Login" to go to login page.
    #. Log in with credentials and set a flag to remember session.
    #. Restart browser and check that user session is saved.

    **Teardown:**

    #. Close browser.
    """
    index_steps.switch_language("en")
    index_steps.goto_login()
    signin_steps.login(config.USER_EMAIL, config.USER_PASSWD,
                       name=config.USER_NAME, remember=True)
    user_account_steps.check_session_saved_after_browser_restart()

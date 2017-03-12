"""
--------------
Register tests
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


def test_register_user_and_login(index_steps,
                                 new_account_steps,
                                 signin_steps,
                                 user_account_steps,
                                 welcome_back_steps):
    """**Scenario:** User signs up, logs out and logs in again.

    **Setup:**

    #. Launch browser and open application URL.

    **Steps:**

    #. Switch language to English.
    #. Sign up with credentials.
    #. Confirm sign up.
    #. Log out.
    #. Go to login page.
    #. Log in with registered credentials.
    #. Log out.

    **Teardown:**

    #. Close browser.
    """
    index_steps.switch_language("en")
    user_data = index_steps.signup()
    new_account_steps.confirm_signup()
    user_account_steps.logout()
    welcome_back_steps.goto_login()
    signin_steps.login(user_data['email'], user_data['password'],
                       name=user_data['name'])
    user_account_steps.logout()


def test_register_postpone(index_steps,
                           new_account_steps,
                           signin_steps,
                           user_account_steps):
    """**Scenario:** User confirms account with next login.

    **Setup:**

    #. Launch browser and open application URL.

    **Steps:**

    #. Switch language to English.
    #. Sign up with credentials.
    #. Reset login session.
    #. Login with registered credentials.
    #. Confirm created account.
    #. Log out.

    **Teardown:**

    #. Close browser.
    """
    index_steps.switch_language("en")
    user_data = index_steps.signup()
    new_account_steps.flush_session()
    signin_steps.check_user_need_confirm_signup_after_login(
        user_data['email'], user_data['password'])
    new_account_steps.confirm_signup()
    user_account_steps.logout()

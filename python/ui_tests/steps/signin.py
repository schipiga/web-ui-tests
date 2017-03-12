"""
------------
Signin steps
------------
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

from hamcrest import equal_to, same_instance

from ui_tests import config
from ui_tests.third_party.matchers import check_that, returns
from ui_tests.third_party import step

from .base import BaseSteps


class SigninSteps(BaseSteps):
    """Sign in page steps."""

    @step.step("Log in with email {1} and password {2}")
    def login(self, email, password, remember=False, name=None, check=True):
        """Step to log in.

        Args:
            email (str): email of user
            password (str): password of user
            name (str, optional): name of user (for verification only)
            check (bool, optional): flag whether to check step or no

        Raises:
            AssertionError: if user didn't log in
        """
        with self.app.page_signin.form_login as form:
            form.field_email.value = email
            form.field_password.value = password
            if remember:
                form.checkbox_remember.click()
            form.submit()
        if check:
            check_that(
                lambda: self.app.current_page,
                returns(same_instance(self.app.page_user_account),
                        timeout=config.PAGE_TIMEOUT),
                "user account page is opened")
            check_that(self.app.page_user_account.label_user_name.value,
                       equal_to(name),
                       "user account page contains user name")

    @step.step("Go to recovery password page")
    def goto_recovery(self, check=True):
        """Step to navigate to recovery password page.

        Args:
            check (bool, optional): flag whether to check step or no

        Raises:
            AssertionError: if navigation didn't happen
        """
        self.app.page_signin.form_login.link_forgot.click()
        if check:
            check_that(lambda: self.app.current_page,
                       returns(same_instance(self.app.page_recovery),
                               timeout=config.PAGE_TIMEOUT),
                       "recovery password page is opened")

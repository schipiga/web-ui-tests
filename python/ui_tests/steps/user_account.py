"""
------------------
User account steps
------------------
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


from hamcrest import same_instance

from ui_tests import config
from ui_tests.third_party.matchers import check_that, returns
from ui_tests.third_party import step

from .base import BaseSteps

__all__ = [
    'UserAccountSteps',
]


class UserAccountSteps(BaseSteps):
    """User account page steps."""

    @step.step("Logout")
    def logout(self, check=True):
        """Step to log out.

        Args:
            check (bool, optional): flag whether to check step or no

        Raises:
            AssertionError: if welcome back page isn't opened
        """
        self.app.page_user_account.link_account_dropdown_menu.click()
        self.app.page_user_account.link_logout.click()

        if check:
            check_that(
                lambda: self.app.current_page,
                returns(same_instance(self.app.page_welcome_back),
                        timeout=config.PAGE_TIMEOUT),
                "welcome back page is opened")

    @step.step("Restart browser and open the same page")
    def _restart_browser(self):
        url = self.app.current_url
        self.app.restart()
        self.app.open(url)

    def check_session_reset_after_browser_restart(self):
        """Step to check that session reset after browser_restart.

        Raises:
            AssertionError: if sign in page isn't opened
        """
        self._restart_browser()
        check_that(
            lambda: self.app.current_page,
            returns(same_instance(self.app.page_signin),
                    timeout=config.PAGE_TIMEOUT),
            "sign in page is opened")

    def check_session_saved_after_browser_restart(self):
        """Step to check that session saved after browser_restart.

        Raises:
            AssertionError: if user account page isn't opened
        """
        self._restart_browser()
        check_that(
            lambda: self.app.current_page,
            returns(same_instance(self.app.page_user_account),
                    timeout=config.PAGE_TIMEOUT),
            "user account page is opened")

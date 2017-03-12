"""
------------------
Welcome back steps
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
    'WelcomeBackSteps',
]


class WelcomeBackSteps(BaseSteps):
    """Welcome back steps."""

    @step.step("Go to login page")
    def goto_login(self, check=True):
        """Step to go to login page.

        Args:
            check (bool, optional): flag whether to check step or no

        Raises:
            AssertionError: if navigation to login page didn't happen
        """
        self.app.page_welcome_back.button_login.click()
        if check:
            check_that(
                lambda: self.app.current_page,
                returns(same_instance(self.app.page_signin),
                        timeout=config.PAGE_TIMEOUT),
                "login page is opened")

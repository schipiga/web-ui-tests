"""
-----------------
New account steps
-----------------
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
from ui_tests.third_party import utils

from .base import BaseSteps

__all__ = [
    'NewAccountSteps',
]


class NewAccountSteps(BaseSteps):
    """New account page steps."""

    @step.step("Confirm new user sign up")
    def confirm_signup(self, company_name=None, check=True):
        """Step to confirm sign up.

        Args:
            company_name (str): name of user's company
            check (bool, optional): flag whether to check step or no

        Raises:
            AssertionError: if account doesn't confirm
        """
        company_name = company_name or next(utils.generate_ids())

        with self.app.page_new_account.form_confirm as form:
            form.field_company_name.value = company_name
            form.combobox_company_industry.value = \
                form.combobox_company_industry.values[1]
            if form.combobox_signup_source.is_present:
                form.combobox_signup_source.value = \
                    form.combobox_signup_source.values[1]
            form.submit()

        if check:
            check_that(lambda: self.app.current_page,
                       returns(same_instance(self.app.page_user_account),
                               timeout=config.PAGE_TIMEOUT),
                       "user account page is opened")

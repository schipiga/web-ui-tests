"""
--------------
Recovery steps
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

from hamcrest import contains_string

from ui_tests import config
from ui_tests.third_party.matchers import check_that, returns
from ui_tests.third_party import step
from ui_tests.third_party import utils

from .base import BaseSteps


class RecoverySteps(BaseSteps):
    """Recovery page steps."""

    @step.step("Recovery password")
    def recovery_password(self, email=None, check=True):
        """Step to recovery password.

        Args:
            email (str, optional): email of recovered user
            check (bool, optional): flag whether to check step or no

        Raises:
            AssertionError: if success notification is absent at page
        """
        email = email or next(utils.generate_ids(postfix='@ex.com'))

        with self.app.page_recovery.block_recovery \
                .form_recovery_password as form:
            form.field_email.value = email
            form.submit()

        if check:
            check_that(
                lambda: self.app.page_recovery.block_recovery.label_description.value,
                returns(contains_string('sent an email containing instructions'),
                        timeout=config.PAGE_TIMEOUT),
                "email with instruction is sent")

    def check_recovery_email_nonexistent_notification(self):
        """Step to check that notification about nonexistent email is present.

        Raises:
            AssertionError: if error message is absent
        """
        self.recovery_password(check=False)
        check_that(
            lambda: self.app.page_recovery.block_recovery.label_error.value,
            returns(contains_string('Incorrect email'),
                    timeout=config.PAGE_TIMEOUT),
            "error message about nonexistent email is present")

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

from hamcrest import assert_that, contains_string

from .base import BaseSteps


class RecoverySteps(BaseSteps):
    """Recovery steps."""

    def recovery_password(self, email, check=True):
        with self.app.page_recovery.block_recovery \
                .form_recovery_password as form:
            form.field_email.value = email
            form.submit()

        if check:
            assert_that(
                self.app.page_recovery.block_recovery.label_description.value,
                contains_string('sent an email containing instructions'))

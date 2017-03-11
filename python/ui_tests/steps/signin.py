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

from hamcrest import assert_that, equal_to, same_instance

from ui_tests.third_party.matchers import returns

from .base import BaseSteps


class SigninSteps(BaseSteps):

    def login(self, email, password, name=None, check=True):
        with self.app.page_signin.form_login as form:
            form.field_email.value = email
            form.field_password.value = password
            form.submit()
        if check:
            assert_that(
                lambda: self.app.current_page,
                returns(same_instance(self.app.page_user_account), timeout=30))
            assert_that(self.app.page_user_account.label_user_name.value,
                        equal_to(name))

    def goto_recovery(self, check=True):
        self.app.page_signin.form_login.link_forgot.click()
        if check:
            assert_that(self.app.current_page,
                        same_instance(self.app.page_recovery))

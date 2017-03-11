# -*- coding: utf-8 -*-

"""
-----------
Index steps
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

from hamcrest import assert_that, equal_to, same_instance

from ui_tests.third_party import step
from ui_tests.third_party.matchers import returns

from .base import BaseSteps


class IndexSteps(BaseSteps):

    @step.step("switch language")
    def switch_language(self, lang, check=True):
        langs = {"en": "English",
                 "ru": u"Русский"}

        self.app.page_index.footer.scroll_to()
        self.app.page_index.footer.combobox_lang.value = langs[lang]

        if check:
            expects = {"en": "Login",
                       "ru": u"Войти"}

            assert_that(lambda: self.app.page_index.button_login.is_present and
                        self.app.page_index.button_login.value,
                        returns(equal_to(expects[lang]), timeout=30))

    @step.step
    def goto_login(self, check=True):
        self.app.page_index.button_login.click()
        if check:
            assert_that(
                lambda: self.app.current_page,
                returns(same_instance(self.app.page_signin), timeout=30))

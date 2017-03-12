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

from hamcrest import equal_to, same_instance

from ui_tests import config
from ui_tests.third_party.matchers import check_that, returns
from ui_tests.third_party import step
from ui_tests.third_party import utils

from .base import BaseSteps


class IndexSteps(BaseSteps):
    """Index page steps."""

    @step.step("Switch language to {1}")
    def switch_language(self, lang, check=True):
        """Step to switch language.

        Args:
            lang (str): switch language code
            check (bool, optional): flag whether to check step or no

        Raises:
            AssertionError: if page will not switched to expected language
        """
        langs = {"en": "English",
                 "ru": u"Русский"}

        self.app.page_index.footer.scroll_to()
        self.app.page_index.footer.combobox_lang.value = langs[lang]

        if check:
            expects = {"en": "Login",
                       "ru": u"Войти"}

            check_that(
                lambda: self.app.page_index.button_login.is_present and
                self.app.page_index.button_login.value,
                returns(equal_to(expects[lang]), timeout=config.PAGE_TIMEOUT),
                "text on login button is changed to language: " + langs[lang])

    @step.step("Go to login page")
    def goto_login(self, check=True):
        """Step to go to login page.

        Args:
            check (bool, optional): flag whether to check step or no

        Raises:
            AssertionError: if navigation to login page didn't happen
        """
        self.app.page_index.button_login.click()
        if check:
            check_that(
                lambda: self.app.current_page,
                returns(same_instance(self.app.page_signin),
                        timeout=config.PAGE_TIMEOUT),
                "login page is opened")

    @step.step("Sign up")
    def signup(self, name=None, email=None, password=None, check=True):
        """Step to sign up.

        Args:
            name (str, optional): name of new user
            email (str, optional): email of new user
            password (str, optional): password of new user
            check (bool, optional): flag whether to check step or no

        Raises:
            AssertionError: if sign up didn't happen
        """
        name = name or next(utils.generate_ids())
        email = email or next(utils.generate_ids(postfix="@ex.com"))
        password = password or next(utils.generate_ids())

        self.app.page_index.button_signup.click()
        with self.app.page_index.form_signup as form:
            form.field_name.value = name
            form.field_email.value = email
            form.field_password.value = password
            form.submit()

        if check:
            check_that(lambda: self.app.current_page,
                       returns(same_instance(self.app.page_new_account),
                               timeout=config.PAGE_TIMEOUT),
                       "new account is created")

        return {'name': name, 'email': email, 'password': password}

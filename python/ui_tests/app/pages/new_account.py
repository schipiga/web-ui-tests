"""
----------------
New account page
----------------
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

from pom import ui
from selenium.webdriver.common.by import By

from ui_tests.app import ui as _ui

from .base import PageBase

__all__ = [
    'PageNewAccount',
]


@ui.register_ui(
    field_company_name=ui.TextField(By.NAME, 'company_name'),
    combobox_company_industry=_ui.ComboBox(By.NAME, 'company_industry'),
    combobox_signup_source=_ui.ComboBox(By.NAME, 'signup_source'))
class FormConfirm(ui.Form):
    """Confirm sign up form."""


@ui.register_ui(
    form_confirm=FormConfirm(By.ID, 'short_signup_step2'))
class PageNewAccount(PageBase):
    """Page opens write after new account creation."""

    url = '/auth/create_new_account'

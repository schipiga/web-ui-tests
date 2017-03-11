"""
------------
Sign in page
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

from pom import ui
from selenium.webdriver.common.by import By

from .base import PageBase

__all__ = [
    'PageSignin',
]


@ui.register_ui(
    field_email=ui.TextField(By.NAME, "login"),
    field_password=ui.TextField(By.NAME, "password"),
    link_forgot=ui.Link(By.CSS_SELECTOR, "a[href*='forgot_password']"))
class FormLogin(ui.Form):
    """Login form."""


@ui.register_ui(
    form_login=FormLogin(By.ID, "login_form"))
class PageSignin(PageBase):
    """Sign in page."""

    url = '/auth/login'

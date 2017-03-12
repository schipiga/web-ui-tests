"""
----------------------
Recovery password page
----------------------
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
    'PageRecovery',
]


@ui.register_ui(
    field_email=ui.TextField(By.NAME, "login"))
class FormRecovery(ui.Form):
    """Recovery password form."""


@ui.register_ui(
    form_recovery_password=FormRecovery(By.ID, "forgot_password_form"),
    label_description=ui.UI(By.CLASS_NAME, "auth-description"),
    label_error=ui.UI(By.CLASS_NAME, 'form_error'))
class BlockRecovery(ui.Block):
    """Recovery block."""


@ui.register_ui(
    block_recovery=BlockRecovery(By.CLASS_NAME, "auth-form-container"))
class PageRecovery(PageBase):
    """Recovery password page."""

    url = '/auth/forgot_password'

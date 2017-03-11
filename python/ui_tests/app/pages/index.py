"""
----------
Index page
----------
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
    'PageIndex',
]


@ui.register_ui(
    button_login=ui.Button(By.CSS_SELECTOR,
                           ".header__navigation__login .btn__label"))
class PageIndex(PageBase):
    """Index page."""

    url = '/'

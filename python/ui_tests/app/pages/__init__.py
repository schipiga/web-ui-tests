"""
-----------------
Application pages
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

from ui_tests.app.pages.index import PageIndex
from ui_tests.app.pages.new_account import PageNewAccount
from ui_tests.app.pages.recovery import PageRecovery
from ui_tests.app.pages.signin import PageSignin
from ui_tests.app.pages.signup import PageSignup
from ui_tests.app.pages.user_account import PageUserAccount

pages = [
    PageIndex,
    PageNewAccount,
    PageRecovery,
    PageSignin,
    PageSignup,
    PageUserAccount,
]

__all__ = [
    'PageIndex',
    'PageNewAccount',
    'PageRecovery',
    'PageSignin',
    'PageSignup',
    'PageUserAccount',

    'pages',
]

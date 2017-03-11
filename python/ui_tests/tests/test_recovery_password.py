"""
-----------------------
Recovery password tests
-----------------------
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


def test_send_recovery_email(index_steps, signin_steps, recovery_steps):
    index_steps.switch_language("en")
    index_steps.goto_login()
    signin_steps.goto_recovery()
    recovery_steps.recovery_password(email="user@example.com")

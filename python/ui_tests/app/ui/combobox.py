"""
------------------
Custom UI ComboBox
------------------
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
from pom.ui.base import timeit, PRESENCE_ERRORS

__all__ = [
    'ComboBox',
]


class ComboBox(ui.ComboBox):
    """Custom combobox."""

    @property
    @timeit
    def is_present(self):
        """Define is combobox present at display."""
        try:
            is_displayed = self.webelement.is_displayed()
            if not is_displayed:
                css_prop = self.webelement.value_of_css_property
                if (css_prop('display') == 'block' and
                        css_prop('visibility') == 'visible' and
                        css_prop('opacity') == '0'):
                    return True
                else:
                    return False
            else:
                return True
        except PRESENCE_ERRORS:
            return False

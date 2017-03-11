"""
--------
Fixtures
--------
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

from ui_tests.fixtures.app import *  # noqa F403
from ui_tests.fixtures.app import __all__ as __all_app__  # noqa F401
from ui_tests.fixtures.index import *  # noqa F403
from ui_tests.fixtures.index import __all__ as __all_index__  # noqa F401
from ui_tests.fixtures.signin import *  # noqa F403
from ui_tests.fixtures.signin import __all__ as __all_signin__  # noqa F401
from ui_tests.fixtures.recovery import *  # noqa F403
from ui_tests.fixtures.recovery import __all__ as __all_recovery__  # noqa F401
from ui_tests.fixtures.report import *  # noqa F403
from ui_tests.fixtures.report import __all__ as __all_report__  # noqa F401

__all__ = (__all_app__ +
           __all_index__ +
           __all_signin__ +
           __all_recovery__ +
           __all_report__)

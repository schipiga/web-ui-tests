"""
--------------
Steps fixtures
--------------
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

import pytest

from ui_tests import steps

__all__ = [
    'index_steps',
    'new_account_steps',
    'recovery_steps',
]


@pytest.fixture
def index_steps(app):
    """Function fixture to get index steps."""
    return steps.IndexSteps(app)


@pytest.fixture
def new_account_steps(app):
    """Function fixture to get new account steps."""
    return steps.NewAccountSteps(app)


@pytest.fixture
def recovery_steps(app):
    """Function fixture to get recovery steps."""
    return steps.RecoverySteps(app)


@pytest.fixture
def signin_steps(app):
    """Function fixture to get signin steps."""
    return steps.SigninSteps(app)

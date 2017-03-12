"""
------------------------
Custom hamcrest matchers
------------------------
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

import allure
from hamcrest import assert_that
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core.raises import DeferredCallable
import waiting

__all__ = [
    'calling',
    'check_that',
    'returns',
]


def check_that(actual, matcher, message):
    """Wrapper over ``assert_that`` to add step in allure report."""
    __tracebackhide__ = True
    with allure.step("Check that " + message):
        assert_that(actual, matcher, message)


class calling(DeferredCallable):
    """Custom ``calling`` to return result after call."""

    def __call__(self):
        return self.func(*self.args, **self.kwargs)


class returns(BaseMatcher):
    """Matcher to check that a result is being matched during timeout."""

    def __init__(self, matcher, timeout):
        self.matcher = matcher
        self.timeout = timeout
        self.last_result = None

    def _matches(self, function):

        def f():
            self.last_result = function()
            return self.matcher.matches(self.last_result)

        try:
            return waiting.wait(f,
                                timeout_seconds=self.timeout,
                                sleep_seconds=0.1)
        except waiting.TimeoutExpired:
            return False

    def describe_to(self, description):
        description.append_description_of(self.matcher).append_text(
            ' during {} sec.'.format(self.timeout))

    def describe_mismatch(self, function, description):
        self.matcher.describe_mismatch(self.last_result, description)

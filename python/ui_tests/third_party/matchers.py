import allure
from hamcrest import assert_that
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.core.raises import DeferredCallable

from ui_tests.third_party.waiter import wait_for


def check_that(actual, matcher, message):
    """
    """
    with allure.step("Check that " + message):
        assert_that(actual, matcher, message)


class calling(DeferredCallable):

    def __call__(self):
        return self.func(*self.args, **self.kwargs)


class returns(BaseMatcher):
    """Matcher to check that a result is being matched during timeout.
    Usage example:
        assert_that(A, returns(has_property('x', 2), timeout=1))
    Result:
        Expected: an object with a property 'x' matching <2> during 1 sec.
             but: property 'x' was <1>
    Variants:
        assert_that(calling(A), returns(has_property('x', 2), timeout=3))
        assert_that(calling(x).with_args(2, 3, y=5), returns(equal_to(7), timeout=1))
        assert_that(lambda: 5, returns(equal_to(2), timeout=5))
        assert_that(calling(lambda x: 5).with_args(x=5), returns(equal_to(5), timeout=1))
    """

    def __init__(self, matcher, timeout):
        self.matcher = matcher
        self.timeout = timeout
        self.last_result = None

    def _matches(self, function):

        def f():
            self.last_result = function()
            return self.matcher.matches(self.last_result)

        return wait_for(self.timeout, f)

    def describe_to(self, description):
        description.append_description_of(self.matcher).append_text(
            ' during {} sec.'.format(self.timeout))

    def describe_mismatch(self, function, description):
        self.matcher.describe_mismatch(self.last_result, description)

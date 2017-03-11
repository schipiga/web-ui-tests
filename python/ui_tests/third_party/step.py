import allure

from ui_tests.third_party import logger

__all__ = [
    'step',
]


def step(obj):

    def wrapper(func):
        return allure_step(logger.log(func))

    if callable(obj):
        allure_step = allure.step
        return wrapper(obj)
    else:
        allure_step = allure.step(obj)
        return wrapper

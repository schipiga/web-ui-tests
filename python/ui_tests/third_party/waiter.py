import abc
import time

__all__ = [
    'Waiter',
    'wait_for',
]


class IWorker(object):
    """object to work one case, just a worker :)
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def exe(self, *args, **kwgs):
        """execute a work
        """


class Waiter(IWorker):

    def __init__(self, polling=0.05):
        self._polling = polling

    def exe(self, timeout, func, *args, **kwgs):
        if not timeout:
            return func(*args, **kwgs) or False
        limit = int(time.time()) + timeout
        while int(time.time()) <= limit:
            result = func(*args, **kwgs)
            if result:
                return result
            time.sleep(self._polling)
        return False


# or just a function
def wait_for(timeout, func, *args, **kwgs):
    if not timeout:
        return func(*args, **kwgs) or False
    limit = int(time.time()) + timeout
    while int(time.time()) <= limit:
        result = func(*args, **kwgs)
        if result:
            return result
        time.sleep(0.05)
    return False

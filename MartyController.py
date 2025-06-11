from martypy import Marty
from martypy.Exceptions import MartyConnectException
from typing import Union


class MartyController:
    def __init__(self, method: str, locator: str = "", blocking: Union[bool, None] = None, *args, **kwargs):
        self.method = method
        self.locator = locator
        self.blocking = blocking
        self.args = args
        self.kwargs = kwargs
        self.marty = None

    def get_ready(self):
        self.marty.get_ready()

    def get_marty(self):
        return self.marty

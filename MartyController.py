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

    def connect(self) -> bool:
        try:
            self.marty = Marty(self.method, self.locator, blocking=self.blocking, *self.args, **self.kwargs)
            print("Successfully connected to Marty!")
            return True
        except MartyConnectException as e:
            print(f"Failed to connect to Marty: {e}")
        except TimeoutError:
            print("Connection to Marty timed out. Please check the IP address or connection settings.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return False
from typing import Optional
from martypy import Marty
from martypy.Exceptions import MartyConnectException

class Moves:
    def __init__(self, marty: Marty):
        self.marty = marty

    def walk(self, num_steps: int = 2, start_foot: str = 'auto', turn: int = 0, step_length: int = 25, move_time: int = 1500, blocking: Optional[bool] = None) -> bool:
        try:
            self.marty.walk(num_steps=num_steps, start_foot=start_foot, turn=turn, step_length=step_length, move_time=move_time, blocking=blocking)
            print("Marty is walking!")
            return True
        except MartyConnectException as e:
            print(f"Failed to make Marty walk: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while walking: {e}")
        return False
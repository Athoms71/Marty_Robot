from martypy.Exceptions import MartyConnectException
from martypy import Marty
from typing import Optional

class Moves:
    def __init__(self, marty: Marty):
        self.marty = marty

    def walkcase(self, case: int = 1):
        self.marty.walk(num_steps=case*7, start_foot='auto', turn=0, step_length=25, move_time=1500, blocking=None)

    def sidestep(self, side: str, steps: int = 2,
                 step_length: int = 35,
                 move_time: int = 1000,
                 blocking: Optional[bool] = None) -> bool:
        try:
            self.marty.sidestep(
                side=side,
                steps=steps,
                step_length=step_length,
                move_time=move_time,
                blocking=blocking
            )
            return True
        except MartyConnectException as e:
            print(f"Failed to make Marty sidestep: {e}")
        except Exception as e:
            print(f"Unexpected error while sidestepping: {e}")
        return False

    def arms(self, left_angle: int, right_angle: int, move_time: int,
             blocking: Optional[bool] = None) -> bool:
        try:
            self.marty.arms(
                left_angle=left_angle,
                right_angle=right_angle,
                move_time=move_time,
                blocking=blocking
            )
            return True
        except MartyConnectException as e:
            print(f"Failed to move Marty's arms: {e}")
        except Exception as e:
            print(f"Unexpected error while moving Marty's arms: {e}")
        return False

    def circle_dance(self, side: str = "right", move_time: int = 2500,
                     blocking: Optional[bool] = None) -> bool:
        try:
            self.marty.circle_dance(
                side=side,
                move_time=move_time,
                blocking=blocking
            )
            print(f"Marty circle_dance!")
            return True
        except MartyConnectException as e:
            print(f"Failed to make Marty circle dance: {e}")
        except Exception as e:
            print(f"Unexpected error while circle dance: {e}")
        return False
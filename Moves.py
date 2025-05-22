from martypy.Exceptions import MartyConnectException
from martypy import Marty
from typing import Optional

class Moves:
    def __init__(self, marty: Marty):
        self.marty = marty

    def get_ready(self, blocking: Optional[bool] = None) -> bool:
        try:
            self.marty.get_ready(blocking=blocking)
            print("Marty is ready!")
            return True
        except MartyConnectException as e:
            print(f"Failed to get Marty ready: {e}")
        except Exception as e:
            print(f"Unexpected error while getting Marty ready: {e}")
        return False

    def walk(self, num_steps: int = 2,
                     start_foot: str = 'auto',
                     turn: int = 0,
                     step_length: int = 25,
                     move_time: int = 1500,
                     blocking: Optional[bool] = None) -> bool:
        try:
            self.marty.walk(
                num_steps=num_steps,
                start_foot=start_foot,
                turn=turn,
                step_length=step_length,
                move_time=move_time,
                blocking=blocking
            )
            print("Marty is walking!")
            return True
        except MartyConnectException as e:
            print(f"Failed to make Marty walk: {e}")
        except Exception as e:
            print(f"Unexpected error while walking: {e}")
        return False

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
            print(f"Marty is sidestepping to the {side}!")
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
            print(f"Marty's arms moved to left: {left_angle}, right: {right_angle}!")
            return True
        except MartyConnectException as e:
            print(f"Failed to move Marty's arms: {e}")
        except Exception as e:
            print(f"Unexpected error while moving Marty's arms: {e}")
        return False

    def dance(self, side: str = "right", move_time: int = 3000,
              blocking: Optional[bool] = None) -> bool:
        try:
            self.marty.dance(
                side=side,
                move_time=move_time,
                blocking=blocking
            )
            print(f"Marty is dancing, starting on the {side} side!")
            return True
        except MartyConnectException as e:
            print(f"Failed to make Marty dance: {e}")
        except Exception as e:
            print(f"Unexpected error while dancing: {e}")
        return False

    def celebrate(self, move_time: int = 4000, blocking: Optional[bool] = None) -> bool:
        try:
            self.marty.celebrate(
                move_time=move_time,
                blocking=blocking
            )
            print(f"Marty celebrate!")
            return True
        except MartyConnectException as e:
            print(f"Failed to make Marty celebrate: {e}")
        except Exception as e:
            print(f"Unexpected error while celebrating: {e}")
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
from martypy.Exceptions import MartyConnectException
from martypy import Marty
from typing import Optional

class Moves:
    def __init__(self, marty: Marty):
        self.marty = marty

    def walkcase(self, case: int = 1, side: str = "forward"):
        if(side == "forward"):
            self.marty.walk(num_steps=case*7, start_foot='auto', turn=0, step_length=25, move_time=1500, blocking=None)
        else:
            self.marty.walk(num_steps=case * 7, start_foot='auto', turn=0, step_length=-25, move_time=1500, blocking=None)

    def sidecase(self, case: int = 1, side: str = "right"):
        self.marty.sidestep(side=side, steps=case*6, step_length=35, move_time=1000, blocking=True)

    def circletime(self, time: int = 1):
        for i in range(time):
            self.marty.circle_dance(side="right", move_time=1000)
            self.marty.circle_dance(side="left", move_time=1000)
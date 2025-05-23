from martypy.Exceptions import MartyConnectException
from martypy import Marty
from typing import Optional

class Moves:
    def __init__(self, marty: Marty):
        self.marty = marty

    def walkcase(self, case: int = 1, side: str = "forward"):
        """
            :param case: Nombre de cases à parcourir. Par défaut, 1.
            :param side: Direction ("forward" ou "backward"). Par défaut, "forward".
        """
        if(side == "forward"):
            self.marty.walk(num_steps=case*7, start_foot='auto', turn=0, step_length=25, move_time=1500, blocking=None)
        else:
            self.marty.walk(num_steps=case * 7, start_foot='auto', turn=0, step_length=-25, move_time=1500, blocking=None)

    def sidecase(self, case: int = 1, side: str = "right"):
        """
            :param case: Nombre de cases à parcourir. Par défaut, 1.
            :param side: Direction ("right" ou "left"). Par défaut, "right".
        """
        self.marty.sidestep(side=side, steps=case*6, step_length=35, move_time=1000, blocking=True)

    def circletime(self, time: int = 1):
        """
            :param time: Nombre de répétitions de la danse circulaire. Par défaut, 1.
        """
        for i in range(time):
            self.marty.arms(left_angle=0, right_angle=135, move_time=500, blocking=False)
            self.marty.circle_dance(side="right", move_time=1000, blocking=False)
            self.marty.arms(left_angle=135, right_angle=0, move_time=500, blocking=False)
            self.marty.circle_dance(side="left", move_time=1000, blocking=False)

    def turn(self, side: str = "left"):
        """
            :param side: Direction du tour ("left" pour gauche ou "right" pour droite). Par défaut, "left".
        """
        if side == "left":
            self.marty.arms(left_angle=0, right_angle=135, move_time=500, blocking=False)
            for i in range(2):
                # Recul du pied gauche
                self.marty.walk(num_steps=1, start_foot='left', turn=0, step_length=-15, move_time=1500)

                # Rotation autour du pied droit
                self.marty.walk(num_steps=1, start_foot='right', turn=30, step_length=0, move_time=1500)
                self.marty.walk(num_steps=1, start_foot='left', turn=0, step_length=0, move_time=1500)
            self.marty.arms(left_angle=0, right_angle=0, move_time=500, blocking=False)
        else:
            self.marty.arms(left_angle=0, right_angle=135, move_time=500, blocking=False)
            for i in range(2):
                # Recul du pied droit
                self.marty.walk(num_steps=1, start_foot='right', turn=0, step_length=-15, move_time=1500)

                # Rotation autour du pied gauche
                self.marty.walk(num_steps=1, start_foot='left', turn=-30, step_length=0, move_time=1500)
                self.marty.walk(num_steps=1, start_foot='right', turn=0, step_length=0, move_time=1500)
            self.marty.arms(left_angle=0, right_angle=0, move_time=500, blocking=False)

    def calibration_path(self):
        path = [
            (2, "left"),
            (1, "left"),
            (2, "right"),
            (1, "right"),
            (2, None)
        ]

        for steps, direction in path:
            self.walkcase(steps)
            if direction:
                self.turn(direction)
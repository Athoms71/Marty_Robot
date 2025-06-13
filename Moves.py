from martypy import Marty
import capteur as C
import file_management as fm
import time


class Moves:
    def __init__(self, marty: Marty):
        """
        Initialise la classe Moves avec une instance de Marty et une position initiale.

        Args:
            marty (Marty): Instance du robot Marty.
        """
        self.marty = marty
        self.pos = [1, 0]  # Position actuelle sur la grille (x, y)

    def get_marty(self):
        """
        Retourne l'instance Marty associée.

        Returns:
            Marty: Instance du robot.
        """
        return self.marty

    def go_to_origin(self, dim: int):
        """
        Ramène le robot au centre de la grille.

        Args:
            dim (int): Dimension de la grille (taille).
        """
        dx = self.pos[0] - (dim - 1) // 2
        dy = self.pos[1] - (dim - 1) // 2

        if dx < 0:
            self.sidecase(-dx)
        elif dx > 0:
            self.sidecase(dx, "left")
        if dy < 0:
            self.walkcase(-dy, "backward")
        elif dy > 0:
            self.walkcase(dy)

        print("Le robot est actuellement au centre de la case")

    def walkcase(self, case: int = 1, side: str = "forward"):
        """
        Fait marcher le robot d'un nombre donné de cases en avant ou en arrière.

        Args:
            case (int): Nombre de cases à parcourir (par défaut 1).
            side (str): Direction du déplacement ("forward" ou "backward").
        """
        if side == "forward":
            self.marty.walk(num_steps=case*7, start_foot='auto',
                            turn=0, step_length=25, move_time=1500, blocking=None)
            self.marty.walk(num_steps=1, start_foot='auto',
                            turn=0, step_length=2, move_time=1500, blocking=True)
            dx, dy = self.pos
            self.pos = (dx, dy + case)
        else:
            self.marty.walk(num_steps=case*7, start_foot='auto',
                            turn=0, step_length=-25, move_time=1500, blocking=None)
            self.marty.walk(num_steps=1, start_foot='auto',
                            turn=0, step_length=-2, move_time=1500, blocking=True)
            dx, dy = self.pos
            self.pos = (dx, dy - case)

    def sidecase(self, case: int = 1, side: str = "right"):
        """
        Fait faire un pas latéral au robot vers la droite ou la gauche.

        Args:
            case (int): Nombre de cases à parcourir (par défaut 1).
            side (str): Direction du déplacement latéral ("right" ou "left").
        """
        self.marty.sidestep(side=side, steps=case*7,
                            step_length=35, move_time=1000, blocking=False)
        dx, dy = self.pos
        if side == "right":
            self.pos = (dx + case, dy)
        else:  # side == "left"
            self.pos = (dx - case, dy)

    def circletime(self, time: int = 1):
        """
        Fait effectuer une danse circulaire au robot un certain nombre de fois.

        Args:
            time (int): Nombre de répétitions de la danse (par défaut 1).
        """
        for _ in range(time):
            self.marty.arms(left_angle=0, right_angle=135,
                            move_time=500, blocking=False)
            self.marty.circle_dance(
                side="right", move_time=1000, blocking=False)
            self.marty.arms(left_angle=135, right_angle=0,
                            move_time=500, blocking=False)
            self.marty.circle_dance(
                side="left", move_time=1000, blocking=False)

    def turn(self, side: str = "left"):
        """
        Fait tourner le robot à gauche ou à droite avec une séquence de pas.

        Args:
            side (str): Direction du tour ("left" ou "right"). Par défaut "left".
        """
        if side == "left":
            self.marty.arms(left_angle=0, right_angle=135,
                            move_time=500, blocking=False)
            for _ in range(2):
                self.marty.walk(num_steps=1, start_foot='left',
                                turn=0, step_length=-15, move_time=1500)
                self.marty.walk(num_steps=1, start_foot='right',
                                turn=30, step_length=0, move_time=1500)
                self.marty.walk(num_steps=1, start_foot='left',
                                turn=0, step_length=0, move_time=1500)
            self.marty.arms(left_angle=0, right_angle=0,
                            move_time=500, blocking=False)
        else:
            self.marty.arms(left_angle=0, right_angle=135,
                            move_time=500, blocking=False)
            for _ in range(2):
                self.marty.walk(num_steps=1, start_foot='right',
                                turn=0, step_length=-15, move_time=1500)
                self.marty.walk(num_steps=1, start_foot='left',
                                turn=-30, step_length=0, move_time=1500)
                self.marty.walk(num_steps=1, start_foot='right',
                                turn=0, step_length=0, move_time=1500)
            self.marty.arms(left_angle=0, right_angle=0,
                            move_time=500, blocking=False)

    def calibration_path(self, size: int):
        """
        Effectue un parcours en spirale pour calibrer les couleurs sur une grille de taille impaire.

        Args:
            size (int): Taille de la grille (doit être un nombre impair >= 1).

        Raises:
            ValueError: Si la taille n'est pas un nombre impair ou inférieure à 1.
        """
        if size % 2 == 0 or size < 1:
            raise ValueError(
                "La taille de la grille doit être un nombre impair et >= 1")

        steps = 1          # Nombre de cases à parcourir dans une direction avant de tourner
        total_steps = 1    # Compteur du nombre total de cases parcourues
        max_steps = size * size  # Nombre total de cases dans la grille

        # Ordre des directions : droite, bas, gauche, haut
        directions = [
            ("sidecase", "right"),
            ("walkcase", "forward"),
            ("sidecase", "left"),
            ("walkcase", "backward")
        ]

        dir_index = 0

        # Crée le fichier pour stocker les couleurs calibrées
        fm.create_file("fichier_couleur", 2)

        # Parcours en spirale sur toute la grille
        while total_steps < max_steps:
            for _ in range(2):  # Répéter deux fois par "tour" de spirale
                action, side = directions[dir_index % 4]
                for _ in range(steps):
                    if total_steps >= max_steps:
                        return
                    getattr(self, action)(1, side)
                    # Calibration couleur sur la case actuelle
                    couleur = ""
                    C.calibrate(self, couleur, "fichier_couleur")
                    total_steps += 1
                dir_index += 1
            steps += 1

        # Position finale en bas à droite
        self.pos = (size - 1, size - 1)

        # Retour au centre
        self.go_to_origin(size)

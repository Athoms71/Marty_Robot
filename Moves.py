from martypy import Marty
import capteur as C
import file_management as fm
from emotions import Emotions
import time


class Moves:
    def __init__(self, marty: Marty):
        """
        Initialise la classe Moves avec une instance de Marty et une position initiale.

        Args:
            marty (Marty): Instance du robot Marty.
        """
        self.marty = marty
        self.pos = [1, 0]
        self.emotions = Emotions(marty)

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

    def react_after_move(self):
        """
        Réagit après un mouvement en fonction de la couleur détectée sous les pieds du robot.
        """
        # Lecture de la couleur sous le robot
        hexa = C.get_feet_colors_hex(self.get_marty())
        if hexa is None:
            print("Erreur : impossible de lire la couleur sous les pieds.")
            return

        # Recherche de la couleur approchée via robert.txt
        couleur = C.get_color_from_hexa(hexa)
        if couleur is None:
            print(
                f"Aucune correspondance trouvée pour la couleur détectée : {hexa}")
            return

        # Lecture du fichier real.feels pour trouver l'émotion associée
        try:
            emotions_table = fm.read_file("real.feels")
        except:
            print("Erreur : impossible de lire le fichier real.feels.")
            return

        # Recherche de l'émotion associée à la couleur
        emotion_to_call = None
        for line in emotions_table:
            color_file, emotion, hexa_code = line
            if color_file.lower() == couleur.lower():
                emotion_to_call = emotion
                break

        if emotion_to_call is None:
            print(f"Aucune émotion définie pour la couleur {couleur}")
            return

        # Appel dynamique de l'émotion sur l'objet Emotions
        if hasattr(self.emotions, emotion_to_call):
            getattr(self.emotions, emotion_to_call)()
        else:
            print(f"L'émotion n'existe pas")

    def walkcase(self, case: int = 1, side: str = "forward", emotion: bool = True):
        """
        Avance ou recule de 'case' cases. Déclenche une émotion si activé.
        :param case: Nombre de cases à parcourir (défaut: 1).
        :param side: "forward" ou "backward" (défaut: forward).
        :param emotion: Active l'émotion après déplacement (défaut: True).
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
        if emotion:  # On déclenche l’émotion uniquement si le booléen est True
            self.react_after_move()

    def sidecase(self, case: int = 1, side: str = "right", emotion: bool = True):
        """
        Déplacement latéral de 'case' cases. Déclenche une émotion si activé.
        :param case: Nombre de cases à parcourir (défaut: 1).
        :param side: "right" ou "left" (défaut: right).
        :param emotion: Active l'émotion après déplacement (défaut: True).
        """
        self.marty.sidestep(side=side, steps=case*7,
                            step_length=35, move_time=1000, blocking=False)
        dx, dy = self.pos
        if side == "right":
            self.pos = (dx + case, dy)
        else:  # side == "left"
            self.pos = (dx - case, dy)
        if emotion:  # On déclenche l’émotion uniquement si le booléen est True
            self.react_after_move()

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
        Tourne sur lui-même à gauche ou à droite.
        :param side: "left" ou "right" (défaut: left).
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
        Effectue un parcours en spirale pour calibrer les couleurs.
        :param size: Taille impaire de la grille (ex: grille 3x3 => 3).
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
                        return  # toutes les cases ont été visitées
                    getattr(self, action)(1, side, emotion=False)
                    # APPEL FONCTION CALIBRATION COULEUR
                    couleur = ""
                    C.calibrate(self, couleur, "fichier_couleur")
                    total_steps += 1
                dir_index += 1
            steps += 1

        # Position finale en bas à droite
        self.pos = (size - 1, size - 1)

        # Retour au centre
        self.go_to_origin(size)

from Moves import Moves
import time
import file_management as F


class Emotions:
    def __init__(self, moves: Moves):
        """
        Initialise l'objet Emotions avec une instance de Moves.

        Args:
            moves (Moves): Instance permettant de contrôler le robot Marty.
        """
        self.moves = moves
        self.robot = moves.get_marty()

    def angry(self):
        """
        Exprime la colère avec des couleurs rouges et un regard en colère.
        """
        self.robot.get_ready()
        self.robot.disco_color("#ff0000")
        self.robot.eyes("angry", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def excited(self):
        """
        Exprime l'excitation avec une couleur jaune vif et un regard excité.
        """
        self.robot.get_ready()
        self.robot.disco_color("#fad700")
        self.robot.eyes("excited", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def normal(self):
        """
        Réinitialise le robot dans un état normal avec une couleur bleue.
        """
        self.robot.get_ready()
        self.robot.disco_color("#0000c0")
        self.robot.eyes("normal", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def wide(self):
        """
        Affiche un regard large avec une couleur bleue claire.
        """
        self.robot.get_ready()
        self.robot.disco_color("#4080ff")
        self.robot.eyes("wide", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def dossier_emotion(self, chemin: str):
        """
        Lit une liste d'émotions depuis un fichier et les joue successivement.

        Args:
            chemin (str): Chemin du fichier contenant les émotions à jouer.

        Note:
            Chaque émotion est un tuple/list avec des informations sur la couleur et l'expression.
        """
        liste_action = F.read_mouv(chemin)
        for emotion in liste_action:
            self.robot.disco_color(emotion[2])
            self.robot.eyes(emotion[1], 50, True)
            time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def wiggle(self):
        """
        Exprime une émotion de "wiggle" avec une couleur violette et un regard spécifique.
        """
        self.robot.get_ready()
        self.robot.disco_color("#e040e0")
        self.robot.eyes("wiggle", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def set_eyes_color(self, color: str):
        """
        Change la couleur des LEDs du robot sans modifier l'expression des yeux.

        Args:
            color (str): Couleur en code hexadécimal (ex: "#ff0000").
        """
        self.robot.get_ready()
        self.robot.disco_color(color)
        time.sleep(0.8)
        self.robot.disco_off()

from Moves import Moves
import time
import file_management as F


class Emotions:
    def __init__(self, moves: Moves):
        self.moves = moves
        self.robot = moves.get_marty()

    def angry(self):
        self.robot.get_ready()
        self.robot.disco_color("#ff0000")
        self.robot.eyes("angry", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def excited(self):
        self.robot.get_ready()
        self.robot.disco_color("#fad700")
        self.robot.eyes("excited", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def normal(self):
        self.robot.get_ready()
        self.robot.disco_color("#0000c0")
        self.robot.eyes("normal", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def wide(self):
        self.robot.get_ready()
        self.robot.disco_color("#4080ff")
        self.robot.eyes("wide", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def dossier_emotion(self, chemin: str):
        liste_action = F.read_mouv(chemin)
        for emotion in liste_action:
            self.robot.disco_color(emotion[2])
            self.robot.eyes(emotion[1], 50, True)
            time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def wiggle(self):
        self.robot.get_ready()
        self.robot.disco_color("#e040e0")
        self.robot.eyes("wiggle", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def set_eyes_color(self, color: str):
        self.robot.get_ready()
        self.robot.disco_color(color)
        time.sleep(0.8)
        self.robot.disco_off()

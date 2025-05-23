from martypy import Marty
import Moves as M
import time


class Emotion:
    def __init__(self, name: str, robot: Marty):
        self.name = name
        self.robot = robot

    def __repr__(self):
        return f"Emotion (name={self.name})"

    def action(self):
        if self.name == "angry":
            self.angry()
            M.Moves(self.robot).get_ready(blocking=True)
        elif self.name == "excited":
            self.excited()
        elif self.name == "normal":
            self.normal()
        elif self.name == "wide":
            self.wide()
        elif self.name == "wiggle":
            self.wiggle()

    def angry(self):
        self.robot.disco_color("red")
        self.robot.eyes("angry", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def excited(self):
        self.robot.disco_color("green")
        self.robot.eyes("excited", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def normal(self):
        self.robot.disco_color("blue")
        self.robot.eyes("normal", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def wide(self):
        self.robot.disco_color("yellow")
        self.robot.eyes("wide", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)

    def wiggle(self):
        self.robot.disco_color("purple")
        self.robot.eyes("wiggle", 50, True)
        time.sleep(0.8)
        self.robot.disco_off()
        self.robot.eyes("normal", 50, True)


try:
    robot = Marty("wifi", "192.168.0.101")
    if not robot.is_conn_ready():
        raise Exception("Marty is not connected")
    else:
        # Initialize the feelings
        angry = Emotion("angry", robot)
        excited = Emotion("excited", robot)
        normal = Emotion("normal", robot)
        wide = Emotion("wide", robot)
        wiggle = Emotion("wiggle", robot)

        # Perform the actions
        angry.action()
        # excited.action()
        # normal.action()
        # wide.action()
        # wiggle.action()

        # Close the connection to the robot
        robot.close()
except Exception as e:
    print(f"Error connecting to Marty: {e}")

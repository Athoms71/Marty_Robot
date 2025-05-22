from martypy import Marty


class Emotion:
    def __init__(self, name: str, robot: Marty):
        self.name = name
        self.robot = robot

    def __repr__(self):
        return f"Emotion (name={self.name})"

    def action(self):
        if self.name == "angry":
            self.angry()
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
        self.robot.eyes("angry", 100, True)
        self.robot.play_sound("angry")
        self.robot.eyes("normal", 100, True)
        self.robot.disco_off()

    def excited(self):
        self.robot.disco_color("green")
        self.robot.eyes("excited", 100, True)
        self.robot.play_sound("excited")
        self.robot.eyes("normal", 100, True)
        self.robot.disco_off()

    def normal(self):
        self.robot.disco_color("blue")
        self.robot.eyes("normal", 100, True)
        self.robot.play_sound("normal")
        self.robot.eyes("normal", 100, True)
        self.robot.disco_off()

    def wide(self):
        self.robot.disco_color("yellow")
        self.robot.eyes("wide", 100, True)
        self.robot.play_sound("wide")
        self.robot.eyes("normal", 100, True)
        self.robot.disco_off()

    def wiggle(self):
        self.robot.disco_color("purple")
        self.robot.eyes("wiggle", 100, True)
        self.robot.play_sound("wiggle")
        self.robot.eyes("normal", 100, True)
        self.robot.disco_off()


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
        excited.action()
        normal.action()
        wide.action()
        wiggle.action()

        # Close the connection to the robot
        robot.close()
except Exception as e:
    print(f"Error connecting to Marty: {e}")

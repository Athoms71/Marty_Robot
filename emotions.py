from martypy import Marty


class Emotion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Emotion(name={self.name})"

    def action(self, robot: Marty):
        if self.name == "angry":
            robot.eyes("angry", 500, True)
            robot.disco_color("red")
        elif self.name == "excited":
            robot.eyes("excited", 500, True)
        elif self.name == "normal":
            robot.eyes("normal", 500, True)
        elif self.name == "wide":
            robot.eyes("wide", 500, True)
        elif self.name == "wiggle":
            robot.eyes("wiggle", 500, True)


try:
    robot = Marty("wifi", "192.168.0.101")
    if not robot.is_conn_ready():
        raise Exception("Marty is not connected")
    else:
        angry = Emotion("angry")
        angry.action(robot)
except Exception as e:
    print(f"Error connecting to Marty: {e}")

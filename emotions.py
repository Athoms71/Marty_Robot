from martypy import Marty


class Emotion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Emotion(name={self.name})"

    def action(self, robot: Marty):
        if self.name == "angry":
            try:
                robot.eyes("angry", 500, True)
            except Exception as e:
                print(f"Error for emotion 'Angry': {e}")
                return False
            return True
        elif self.name == "excited":
            try:
                robot.eyes("excited", 500, True)
            except Exception as e:
                print(f"Error for emotion 'Excited': {e}")
                return False
            return True
        elif self.name == "normal":
            try:
                robot.eyes("normal", 500, True)
            except Exception as e:
                print(f"Error for emotion 'Normal': {e}")
                return False
            return True
        elif self.name == "wide":
            try:
                robot.eyes("wide", 500, True)
            except Exception as e:
                print(f"Error for emotion 'Wide': {e}")
                return False
            return True
        elif self.name == "wiggle":
            try:
                robot.eyes("wiggle", 500, True)
            except Exception as e:
                print(f"Error for emotion 'Wiggle': {e}")
                return False
            return True
        else:
            return "I have no emotion."


try:
    robot = Marty("wifi", "192.168.0.101")
except Exception as e:
    print(f"Error connecting to Marty: {e}")

angry = Emotion("angry")
angry.action(robot)
excited = Emotion("excited")
excited.action(robot)
normal = Emotion("normal")
normal.action(robot)
wide = Emotion("wide")
wide.action(robot)
wiggle = Emotion("wiggle")
wiggle.action(robot)

from martypy import Marty


class Gesture:
    def __init__(self, name: str, robot: Marty):
        self.name = name
        self.robot = robot

    def __repr__(self):
        return f"Emotion (name={self.name})"

    def action(self):
        if self.name == "christmas":
            self.christmas()
        """elif self.name == "excited":
            self.excited()
        elif self.name == "normal":
            self.normal()
        elif self.name == "wide":
            self.wide()
        elif self.name == "wiggle":
            self.wiggle()"""

    def christmas(self):
        sent = self.robot.send_file("musics/jingle_bells.mp3")
        if sent:
            print("File sent successfully")
        else:
            print("Failed to send file")
        self.robot.play_mp3("fs/jingle_bells.mp3")
        for i in range(100):
            self.robot.disco_color("red")
            self.robot.eyes(45, 200, False)
            self.robot.disco_color("green")
            self.robot.eyes(0, 200, False)
        self.robot.eyes("normal", 200, True)
        self.robot.disco_off()


try:
    robot = Marty("wifi", "192.168.0.101")
    if not robot.is_conn_ready():
        raise Exception("Marty is not connected")
    else:
        # Initialize the gestures
        christmas = Gesture("christmas", robot)

        # Perform the actions
        christmas.action()

        # Close the connection to the robot
        robot.close()
except Exception as e:
    print(f"Error connecting to Marty: {e}")

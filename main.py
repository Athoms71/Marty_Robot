from MartyController import MartyController

if __name__ == "__main__":
    controller = MartyController(method="wifi", locator="192.168.0.101")
    if controller.connect():
        controller.marty.dance()
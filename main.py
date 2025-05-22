import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from MartyController import MartyController
from MainWindow import MainWindow
from Moves import Moves
import capteur

def main():
    # Connect to Marty
    martyController = MartyController(method="wifi", locator="192.168.0.101")
    if not martyController.connect():
        sys.exit(1)

    # Initialize QApplication
    app = QApplication(sys.argv)
    capteur.Capteur.battery(controller.marty)
    capteur.Capteur.colorsensor(controller.marty)
    capteur.Capteur.distance(controller.marty)
    capteur.Capteur.obsacle(controller.marty)

    martyController.get_ready()
    marty = martyController.get_marty()
    moves = Moves(marty)

    window = MainWindow(moves)
    window.show()
    # Main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from MartyController import MartyController
from MainWindow import MainWindow
from Moves import Moves

def main():
    # Connect to Marty
    martyController = MartyController(method="wifi", locator="192.168.0.101")
    if not martyController.connect():
        sys.exit(1)

    # Initialize QApplication
    app = QApplication(sys.argv)

    martyController.get_ready()
    marty = martyController.get_marty()
    moves = Moves(marty)

    moves.walkcase(1)

    window = MainWindow(moves)
    window.show()
    # Main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
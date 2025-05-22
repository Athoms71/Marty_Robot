import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from MartyController import MartyController
from MainWindow import MainWindow
from Moves import Moves

def main():
    # Connect to Marty
    controller = MartyController(method="wifi", locator="192.168.0.101")
    #if not controller.connect():
    #    sys.exit(1)

    # Initialize QApplication
    app = QApplication(sys.argv)

    moves = Moves(controller.marty)
    moves.get_ready()
    window = MainWindow(moves)
    window.show()
    # Main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
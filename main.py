import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from martypy import Marty

from MartyController import MartyController
from MainWindow import MainWindow
from Moves import Moves

def main():
    # Connect to Marty
    marty = Marty(method="wifi", locator="192.168.0.101")
    if not marty.is_conn_ready():
        raise Exception("Marty is not connected")

    # Initialize QApplication
    app = QApplication(sys.argv)

    marty.get_ready()
    moves = Moves(marty)

    window = MainWindow(moves)
    window.show()
    # Main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
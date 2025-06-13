import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from martypy import Marty
import file_management as file_management
from MainWindow import MainWindow
from Moves import Moves
from Sequential import Sequential
import capteur
from emotions import *
from MainWindow import MainWindow


def main():
    # Connect to Marty
    marty = Marty(method="wifi", locator="192.168.1.5")
    if not marty.is_conn_ready():
        raise Exception("Marty is not connected")
    else:
        print("Marty connected !")
    
    # Initialize QApplication
    app = QApplication(sys.argv)
 

    marty.get_ready()
    #marty = None

    moves = Moves(marty)
    sequential = Sequential(moves)

    window = MainWindow(moves, sequential)
    window.show()
    # Main loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


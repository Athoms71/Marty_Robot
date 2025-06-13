import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from Moves import Moves
from Sequential import Sequential
from capteur import Capteur
from emotions import Emotions
from ConnectWindow import ConnectWindow

def main():
    app = QApplication(sys.argv)

    connect_window = ConnectWindow()
    connect_window.show()

    app.main_window = None

    def on_marty_connected(marty):
        print("Optimus Prime connected")
        marty.get_ready()

        moves = Moves(marty)
        sequential = Sequential(moves)
        capteur = Capteur(marty)

        app.main_window = MainWindow(moves, sequential, capteur)
        app.main_window.show()

    connect_window.marty_connected.connect(on_marty_connected)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

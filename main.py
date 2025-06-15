import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from Moves import Moves
import capteur
from emotions import *
from MainWindow import MainWindow
from ConnectWindow import ConnectWindow
from Sequential import Sequential
from capteur import Capteur

def main():
    app = QApplication(sys.argv)

    connect_window = ConnectWindow()
    connect_window.show()

    app.main_window = None # MainWindow sera créé après la connexion

    def on_marty_connected(marty):
        print("Optimus Prime connected")
        marty.get_ready() # Prépare le robot après connexion

        # Initialisation des modules principaux
        moves = Moves(marty)
        sequential = Sequential(moves)
        capteur = Capteur(marty)

        # Création et affichage de la fenêtre principale
        app.main_window = MainWindow(moves, sequential, capteur)
        app.main_window.show()

    connect_window.marty_connected.connect(on_marty_connected)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

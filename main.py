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
    """
    Point d'entrée principal de l'application.

    Cette fonction initialise l'application PyQt, crée la fenêtre de connexion,
    et établit une connexion avec le robot Marty. Une fois connecté, elle instancie
    les modules Moves, Sequential et Capteur, puis ouvre la fenêtre principale
    de contrôle du robot.

    Elle gère la boucle événementielle Qt et se termine proprement lors de la fermeture.

    Args:
        Aucun.

    Returns:
        Aucun.
    """
    app = QApplication(sys.argv)

    connect_window = ConnectWindow()
    connect_window.show()

    app.main_window = None # MainWindow sera créé après la connexion

    def on_marty_connected(marty):
        """
        Slot appelé lorsque la connexion au robot Marty est établie.

        Prépare le robot, crée les modules nécessaires et affiche la fenêtre principale.

        Args:
            marty (Marty): Instance connectée du robot Marty.
        """
        print("Optimus Prime connected")

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

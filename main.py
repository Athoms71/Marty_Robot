import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from MartyController import MartyController
from MainWindow import MainWindow
from Moves import Moves

def main():
    # Initialiser QApplication
    app = QApplication(sys.argv)

    # Connecter Marty
    controller = MartyController(method="wifi", locator="192.168.0.101", blocking=False, timeout=5)
    if not controller.connect():
        QMessageBox.critical(None, "Erreur de connexion",
                             "Impossible de se connecter à Marty.\n"
                             "Vérifie l'adresse IP et le réseau.")
        sys.exit(1)

    moves = Moves(controller.marty)
    window = MainWindow(moves)
    window.show()
    moves.get_ready(blocking=True)

    # Boucle principale
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
from MartyController import MartyController
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from martypy import Marty
from MainWindow import MainWindow
from Moves import Moves


def main():
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    # Code à mettre dans la classe MartyRobot lors de l'initialisation
    """
    try:
        marty = Marty("wifi","192.168.0.101")
    except Exception as e:
        QMessageBox.critical(None, "Erreur de connexion", 
                             f"Impossible de se connecter à Marty:\n{e}")
        sys.exit(1)
    """

    fen = MainWindow()
    fen.show()
    app.exec_()

if __name__ == "__main__":
    controller = MartyController(method="wifi", locator="192.168.0.101")
    if controller.connect():
        walker = Moves(controller.marty)
        walker.walk(num_steps=10, start_foot='auto', turn=0, step_length=25, move_time=1500)
    main()

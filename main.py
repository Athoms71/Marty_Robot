import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from martypy import Marty
import file_management as fm
import MainWindow
import Moves


def connect_Marty(ip_address: str = "192.168.0.101"):
    """Connect to Marty using the given IP address."""
    try:
        marty = Marty(method="wifi", locator=ip_address)
        if not marty.is_conn_ready():
            raise Exception("Marty is not connected")
        return marty
    except Exception as e:
        QMessageBox.critical(None, "Connection Error", str(e))
        sys.exit(1)
    return marty


def create_grid():
    couleurs_theoriques = fm.read_file("calibration.txt")
    grid = [["" for _ in range(3)] for _ in range(3)]
    # TODO : Initialiser la grille avec les couleurs détectées


def main():
    # Initialize the connection to Marty
    marty = connect_Marty()

    # Create the grid
    grid = create_grid()

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

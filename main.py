import sys
# from PyQt5.QtWidgets import QApplication, QMessageBox
from martypy import Marty
import file_management as fm
# import MainWindow
from Moves import Moves


def connect_Marty(ip_address: str = "192.168.0.102"):
    """Connect to Marty using the given IP address."""
    try:
        marty = Marty(method="wifi", locator=ip_address)
        if not marty.is_conn_ready():
            raise Exception("Marty is not connected")
        return marty
    except Exception as e:
        # QMessageBox.critical(None, "Connection Error", str(e))
        sys.exit(1)
    return marty


def create_grid():
    couleurs_theoriques = fm.read_file("calibration.txt")
    cm = fm.read_file("couleur_parcours.txt")
    grid = [["" for _ in range(3)] for _ in range(3)]
    # TODO : Initialiser la grille avec les couleurs détectées
    for i in range(3):
        for j in range(3):
            delta = 5
            for color, value in couleurs_theoriques:
                if (cm[0] > value[0]-delta and cm[0] < value[0]+delta) and (cm[1] > value[1]-delta and cm[1] < value[1]+delta):
                    grid[i][j] = color
    return grid


def main():
    # Initialize the connection to Marty
    marty = connect_Marty()

    # Create the grid
    grid = create_grid()
    print(grid)

    # Initialize QApplication
    # app = QApplication(sys.argv)

    marty.get_ready()
    moves = Moves(marty)
    # window = MainWindow(moves)
    # window.show()

    # Main loop
    # sys.exit(app.exec_())


if __name__ == "__main__":
    main()

from PyQt5.QtWidgets import QWidget, QPushButton
from martypy import Marty
import sys
from PyQt5.QtWidgets import QApplication
from random import randint


class AbsoluteWindow(QWidget):
    def __init__(self, dim: int):
        super().__init__()
        self.dim = dim
        self.setWindowTitle("Construction du parcours en absolu")
        self.setFixedSize(150*self.dim, 130*self.dim)

        # Boutons pour créer la grille à partir de la dimension
        for row in range(dim):
            for col in range(dim):
                tmp_button = QPushButton(f"{row},{col}", self)
                tmp_button.setFixedSize(75, 75)
                tmp_button.move(self.width()//4+(75*col),
                                10*self.dim+(75*row+row*5))
                tmp_button.clicked.connect(
                    lambda _, r=row, c=col: self.handle_cell_click(r, c))

        # Bouton central pour quitter
        self.exit_button = QPushButton("Quitter", self)
        self.exit_button.setFixedSize(self.dim*20, 50)
        self.exit_button.move(
            self.width() // 2-self.dim*10, self.height() - 10*self.dim-50)
        self.exit_button.clicked.connect(self.closeEvent)  # Ferme la fenêtre
        self.show()

    def handle_cell_click(self, row: int, col: int):
        ACTIONS.append(f"{row}{col}")

    def save_abs(self, file_path: str):
        if file_path.endswith(".dance"):
            with open(file_path, "w") as fichier:
                fichier.write(f"ABS {self.dim}\n")
                for move in ACTIONS:
                    fichier.write(f"{move}\n")
            print("Fichier enregistré avec succès.")
        else:
            print("Le fichier est introuvable.")

    def closeEvent(self, event):
        self.save_abs(f"{randint(0, 1000)}_auto.dance")
        self.close()


app = QApplication(sys.argv)
ACTIONS = []
window = AbsoluteWindow(5)
window.show()
sys.exit(app.exec_())

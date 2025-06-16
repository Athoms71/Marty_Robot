from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from martypy import Marty
import sys
from random import randint


class AbsoluteWindow(QWidget):
    def __init__(self, dim: int, file_name: str, main_window):
        """
        Initialise la fenêtre avec une grille de boutons.

        Args:
            dim (int): Dimension de la grille (nombre de lignes et colonnes).
        """
        super().__init__()
        self.main_window = main_window
        self.dim = dim
        self.file_name = file_name
        self.list_actions = []  # Stocke les actions (clics sur les boutons)
        self.setWindowTitle("Construction du parcours en absolu")
        self.setFixedSize(150 * dim, 130 * dim)

        # Création d'une grille de boutons selon la dimension donnée
        for col in range(dim):
            for row in range(dim):
                btn = QPushButton(f"{row},{col}", self)
                btn.setFixedSize(75, 75)
                btn.move(self.width() // 4 + 75 * col,
                         10 * dim + (75 * row + 5 * row))
                # Connexion du clic avec les coordonnées de la cellule
                btn.clicked.connect(
                    lambda _, r=row, c=col: self.handle_cell_click(r, c))

        button_width = dim * 20
        button_height = 50
        spacing = 20  # espace entre les boutons

        total_width = button_width * 2 + spacing
        start_x = (self.width() - total_width) // 2
        y_pos = self.height() - button_height - 20  # 20 px au-dessus du bord bas

        # Bouton "Quitter"
        self.exit_button = QPushButton("Quitter", self)
        self.exit_button.setFixedSize(button_width, button_height)
        self.exit_button.move(start_x, y_pos)
        self.exit_button.clicked.connect(self.close)

        # Bouton "Save"
        self.save_btn = QPushButton("Save", self)
        self.save_btn.setFixedSize(button_width, button_height)
        self.save_btn.move(start_x + button_width + spacing, y_pos)
        self.save_btn.clicked.connect(self.save_abs)

        self.show()

    def handle_cell_click(self, row: int, col: int):
        """
        Gère le clic sur une cellule de la grille.

        Args:
            row (int): Indice de la ligne du bouton cliqué.
            col (int): Indice de la colonne du bouton cliqué.
        """
        # Ajoute la position cliquée à la liste d'actions
        self.list_actions.append(f"{row}{col}")

    def save_abs(self):
        """
        Sauvegarde la liste des mouvements dans un fichier .dance.

        Args:
            file_path (str): Chemin où enregistrer la séquence.

        Note:
            Le fichier est écrit uniquement si l'extension est '.dance'.
        """
        if self.file_name.endswith(".dance"):
            with open(self.file_name, "w") as fichier:
                fichier.write(f"ABS {self.dim}\n")
                for action in self.list_actions:
                    fichier.write(f"{action}\n")
            print("Fichier enregistré avec succès.")
        else:
            print("Le fichier est introuvable.")

    def closeEvent(self, event):
        # Rétablir le mode dans la fenêtre principale
        self.main_window.mode = 0
        self.main_window.update_icon_modes()
        self.main_window.absolute_window = None
        event.accept()

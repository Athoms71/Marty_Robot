from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from martypy import Marty
import sys
from random import randint


class AbsoluteWindow(QWidget):
    def __init__(self, dim: int):
        """
        Initialise la fenêtre avec une grille de boutons.

        Args:
            dim (int): Dimension de la grille (nombre de lignes et colonnes).
        """
        super().__init__()
        self.dim = dim
        self.list_actions = []  # Stocke les actions (clics sur les boutons)
        self.setWindowTitle("Construction du parcours en absolu")
        self.setFixedSize(150 * dim, 130 * dim)

        # Création d'une grille de boutons selon la dimension donnée
        for row in range(dim):
            for col in range(dim):
                btn = QPushButton(f"{row},{col}", self)
                btn.setFixedSize(75, 75)
                btn.move(self.width() // 4 + 75 * col,
                         10 * dim + (75 * row + 5 * row))
                # Connexion du clic avec les coordonnées de la cellule
                btn.clicked.connect(
                    lambda _, r=row, c=col: self.handle_cell_click(r, c))

        # Bouton "Quitter" centré en bas
        self.exit_button = QPushButton("Quitter", self)
        self.exit_button.setFixedSize(dim * 20, 50)
        self.exit_button.move(self.width() // 2 - dim *
                              10, self.height() - 10 * dim - 50)
        self.exit_button.clicked.connect(self.closeEvent)  # Fermer la fenêtre
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

    def save_abs(self, file_path: str):
        """
        Sauvegarde la liste des actions dans un fichier au format '.dance'.

        Args:
            file_path (str): Chemin du fichier où enregistrer les actions.

        Note:
            Le fichier est écrit uniquement si l'extension est '.dance'.
        """
        if file_path.endswith(".dance"):
            with open(file_path, "w") as f:
                f.write(f"ABS {self.dim}\n")
                for move in self.list_actions:
                    f.write(f"{move}\n")
            print("Fichier enregistré avec succès.")
        else:
            print("Le fichier est introuvable.")

    def closeEvent(self, event=None):
        """
        Gère la fermeture de la fenêtre.

        Args:
            event (QCloseEvent, optional): Événement de fermeture.

        Sauvegarde automatiquement la liste des actions dans un fichier
        avec un nom aléatoire si des actions ont été enregistrées.
        """
        if event is None:
            if self.list_actions:
                self.save_abs(f"{randint(0, 1000)}_auto.dance")
            self.close()

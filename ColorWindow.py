from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit


class ColorWindow(QDialog):
    def __init__(self, moves_class):
        super().__init__()
        self.moves_class = moves_class
        self.setWindowTitle("Choix de couleur")
        self.setFixedSize(400, 300)
        self.setModal(True)  # Rend la fenêtre bloquante

        # Champ de saisie
        self.input_color = QLineEdit(self)
        self.input_color.setPlaceholderText("Entrez la couleur")
        self.input_color.setFixedSize(200, 50)
        self.input_color.move(self.width() // 2 - 100, self.height() // 4)
        self.input_color.setStyleSheet("background-color: white; font-size: 14px; padding: 2px;")

        # Bouton "Valider"
        self.valide_button = QPushButton("Valider", self)
        self.valide_button.setFixedSize(100, 50)
        self.valide_button.move(self.width() // 2 - 50, self.height() - 100)
        self.valide_button.clicked.connect(self.on_validate)

    def on_validate(self):
        self.moves_class.color = self.input_color.text()
        self.accept()  # Ferme le QDialog proprement et débloque le code appelant

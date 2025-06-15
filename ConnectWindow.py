from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal
from martypy import Marty


class ConnectWindow(QWidget):
    """
    Fenêtre de connexion à Marty via Wi-Fi.

    Cette classe permet à l'utilisateur d'entrer l'adresse IP du robot Marty, 
    d'établir la connexion et d'émettre un signal lorsque la connexion est réussie.

    Attributes:
        marty_connected (pyqtSignal): Signal émis avec l'objet Marty connecté.
    """

    # Signal émis si Marty est connecté avec succès
    marty_connected = pyqtSignal(object)

    def __init__(self):
        """
        Initialise la fenêtre de connexion avec un champ IP et un bouton Connecter.
        """
        super().__init__()
        self.setWindowTitle("Connexion à Optimus Prime")
        self.resize(300, 150)

        self.ip_input = QLineEdit(self)
        self.ip_input.setPlaceholderText("192.168.1.2")

        self.connect_btn = QPushButton("Connecter", self)
        self.connect_btn.clicked.connect(self.connect_to_marty)

        layout = QVBoxLayout()
        layout.addWidget(self.ip_input)
        layout.addWidget(self.connect_btn)
        self.setLayout(layout)

    def connect_to_marty(self):
        """
        Tente de se connecter au robot Marty à l'adresse IP donnée.

        - Récupère l'adresse IP entrée par l'utilisateur.
        - Tente d'instancier un objet Marty en mode Wi-Fi avec cette IP.
        - Si la connexion est prête, émet le signal `marty_connected` avec l'objet Marty.
        - Sinon, affiche un message d'erreur.

        Returns:
            None
        """
        ip = self.ip_input.text().strip()
        if not ip:
            QMessageBox.warning(
                self, "Erreur", "Veuillez entrer une adresse IP.")
            return

        try:
            marty = Marty(method="wifi", locator=ip)
            if not marty.is_conn_ready():
                raise Exception("Connexion échouée")
            QMessageBox.information(self, "Succès", "Marty est connecté !")
            self.marty_connected.emit(marty)  # Émet le Marty connecté
            self.close()
        except Exception as e:
            QMessageBox.critical(
                self, "Erreur", f"Échec de la connexion à Marty : {str(e)}")

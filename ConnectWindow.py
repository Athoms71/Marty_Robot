from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal
from martypy import Marty

class ConnectWindow(QWidget):
    marty_connected = pyqtSignal(object)  # Signal émis si Marty est connecté avec succès

    def __init__(self):
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
        ip = self.ip_input.text().strip()
        if not ip:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer une adresse IP.")
            return

        try:
            marty = Marty(method="wifi", locator=ip)
            if not marty.is_conn_ready():
                raise Exception("Connexion échouée")
            QMessageBox.information(self, "Succès", "Marty est connecté !")
            self.marty_connected.emit(marty)  # Émet le Marty connecté
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Échec de la connexion à Marty : {str(e)}")

from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QTimer, QPoint
from PyQt5.QtGui import QCursor
from martypy import Marty


class MouseTrackingWindow(QWidget):
    """
    Fenêtre PyQt5 permettant de contrôler le robot Marty via les mouvements de la souris.

    Attributs:
        marty (Marty): Instance du robot Marty à contrôler.
        main_window (QWidget): Référence à la fenêtre principale (MainWindow).
        timer (QTimer): Timer pour actualiser périodiquement la direction du robot.
        exit_button (QPushButton): Bouton pour quitter la fenêtre.
    """

    def __init__(self, marty: Marty, main_window):
        """
        Initialise la fenêtre de contrôle par la souris.

        Args:
            marty (Marty): L’instance du robot à contrôler.
            main_window (QWidget): La fenêtre principale pour mise à jour de l’état.
        """
        super().__init__()
        self.marty = marty
        self.main_window = main_window
        self.setWindowTitle("Contrôle du robot par la souris")
        self.setFixedSize(600, 600)
        self.setMouseTracking(True)

        # Timer déclenché toutes les 1000 ms pour mettre à jour la direction du robot
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_robot_direction)
        self.timer.start(1000)

        # Bouton "Quitter" centré pour fermer la fenêtre
        self.exit_button = QPushButton("Quitter", self)
        self.exit_button.setFixedSize(100, 100)
        self.exit_button.move(self.width() // 2 - 50, self.height() // 2 - 50)
        self.exit_button.clicked.connect(self.close)

        self.show()

    def update_robot_direction(self):
        """
        Met à jour la direction et le mouvement du robot selon la position actuelle de la souris.

        Calcule le décalage (dx, dy) par rapport au centre de la fenêtre.
        Si la souris est dans une zone morte centrale (±50 pixels), le robot ne bouge pas.
        Sinon, ajuste l’angle de rotation (turn) selon dx et la longueur du pas (step_length) selon dy.
        Démarre une marche du robot avec ces paramètres.
        """
        try:
            global_pos = QCursor.pos()
            local_pos = self.mapFromGlobal(global_pos)
            center = QPoint(self.width() // 2, self.height() // 2)

            dx = local_pos.x() - center.x()
            dy = center.y() - local_pos.y()

            if abs(dx) < 50 and abs(dy) < 50:
                print("Zone centrale - pas de mouvement")
                return

            turn = 0
            if dx > 50:
                turn = -15
            elif dx < -50:
                turn = 15

            step_length = 25 if dy > 0 else -25
            distance = abs(dy)
            move_time = max(800, 2000 - distance * 5)

            print(
                f"dx={dx}, dy={dy}, turn={turn}, step_length={step_length}, move_time={move_time}")
            self.marty.walk(num_steps=1, start_foot='auto', turn=turn,
                            step_length=step_length, move_time=move_time, blocking=False)

            self.timer.start(move_time + 100)

        except Exception as e:
            print(f"Error during robot movement: {e}")

    def closeEvent(self, event):
        """
        Gère la fermeture de la fenêtre.

        Met à jour le mode de la fenêtre principale à 0,
        met à jour les icônes, et nettoie la référence à cette fenêtre.
        Accepte l’événement de fermeture.

        Args:
            event (QCloseEvent): L’événement de fermeture de la fenêtre.
        """
        self.main_window.mode = 0
        self.main_window.update_icon_modes()
        self.main_window.mouse_tracking_window = None
        event.accept()

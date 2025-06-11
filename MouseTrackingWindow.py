import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, Qt, QPoint
from PyQt5.QtGui import QCursor, QPainter, QColor
from martypy import Marty

class MouseTrackingWindow(QWidget):
    def __init__(self, marty: Marty):
        super().__init__()
        self.marty = marty  # Instance de ton robot
        self.setWindowTitle("Contrôle du robot par la souris")
        self.setFixedSize(600, 600)
        self.dead_zone_size = 100
        self.setMouseTracking(True)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_robot_direction)
        self.timer.start(1000)

        self.show()

    def paintEvent(self, event):
        # Affiche un carré gris au centre = zone morte
        painter = QPainter(self)
        painter.setBrush(QColor(180, 180, 180))
        center_x = self.width() // 2 - self.dead_zone_size // 2
        center_y = self.height() // 2 - self.dead_zone_size // 2
        painter.drawRect(center_x, center_y, self.dead_zone_size, self.dead_zone_size)

    def update_robot_direction(self):
        try:
            # Obtenir la position de la souris globalement et localement
            global_pos = QCursor.pos()
            local_pos = self.mapFromGlobal(global_pos)
            center = QPoint(self.width() // 2, self.height() // 2)

            dx = local_pos.x() - center.x()
            dy = center.y() - local_pos.y()  # inversé car y augmente vers le bas

            if abs(dx) < self.dead_zone_size // 2 and abs(dy) < self.dead_zone_size // 2:
                print("Zone centrale - pas de mouvement")
                return  # Trop proche du centre, ne bouge pas

            # Calcul de la direction du mouvement
            turn = 0
            if dx > 50:
                turn = -15  # Tourne vers la droite
            elif dx < -50:
                turn = 15  # Tourne vers la gauche

            # Marche avant ou arrière
            step_length = 25 if dy > 0 else -25

            # Vitesse dépend de la distance verticale
            distance = abs(dy)
            move_time = max(800, 2000 - distance * 5)  # entre 600ms et 2000ms

            print(f"dx={dx}, dy={dy}, turn={turn}, step_length={step_length}, move_time={move_time}")
            self.marty.walk(num_steps=1, start_foot='auto', turn=turn, step_length=step_length, move_time=move_time, blocking=False)

            # Adapter la fréquence du timer dynamiquement
            self.timer.start(move_time + 100)

        except Exception as e:
            print(f"Error during robot movement: {e}")
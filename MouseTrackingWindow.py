from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QTimer, QPoint
from PyQt5.QtGui import QCursor
from martypy import Marty

class MouseTrackingWindow(QWidget):
    def __init__(self, marty: Marty, main_window):
        super().__init__()
        self.marty = marty
        self.main_window = main_window  # Référence à MainWindow
        self.setWindowTitle("Contrôle du robot par la souris")
        self.setFixedSize(600, 600)
        self.setMouseTracking(True)

        # Timer pour bouger le robot régulièrement
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_robot_direction)
        self.timer.start(1000)

        # Bouton central pour quitter
        self.exit_button = QPushButton("Quitter", self)
        self.exit_button.setFixedSize(100, 100)
        self.exit_button.move(self.width() // 2 - 50, self.height() // 2 - 50)
        self.exit_button.clicked.connect(self.close)  # Ferme la fenêtre

        self.show()

    def update_robot_direction(self):
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

            print(f"dx={dx}, dy={dy}, turn={turn}, step_length={step_length}, move_time={move_time}")
            self.marty.walk(num_steps=1, start_foot='auto', turn=turn,
                            step_length=step_length, move_time=move_time, blocking=False)

            self.timer.start(move_time + 100)

        except Exception as e:
            print(f"Error during robot movement: {e}")

    def closeEvent(self, event):
        # Reset
        self.main_window.mode = 0
        self.main_window.update_icon_modes()
        self.main_window.mouse_tracking_window = None
        event.accept()

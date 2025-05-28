from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt, QRect
import sys, os

class MainWindow(QWidget):
    def __init__(self, moves):
        super().__init__()
        self.setWindowTitle("Optimus Prime")
        self.resize(1280, 720)

        self.moves = moves
        self.list_mode = False

        palette = QPalette()
        pix = QPixmap('image/background.jpg').scaled(self.size(), Qt.KeepAspectRatioByExpanding)
        palette.setBrush(QPalette.Window, QBrush(pix))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Forward Button
        btn_forward = QPushButton(self)
        btn_forward.setIcon(QIcon("buttons/btn_forward.png"))
        btn_forward.setFixedSize(100, 100)
        btn_forward.setIconSize(btn_forward.size())
        btn_forward.setStyleSheet("border: none; padding: 0px;")
        btn_forward.clicked.connect(self.on_forwardBtn_clicked)

        # right Button
        btn_right = QPushButton(self)
        btn_right.setIcon(QIcon("buttons/btn_right.png"))
        btn_right.setFixedSize(100, 100)
        btn_right.setIconSize(btn_right.size())
        btn_right.setStyleSheet("border: none; padding: 0px;")
        btn_right.clicked.connect(self.on_rightBtn_clicked)

        # backward Button
        btn_backward = QPushButton(self)
        btn_backward.setIcon(QIcon("buttons/btn_backward.png"))
        btn_backward.setFixedSize(100, 100)
        btn_backward.setIconSize(btn_backward.size())
        btn_backward.setStyleSheet("border: none; padding: 0px;")
        btn_backward.clicked.connect(self.on_backwardBtn_clicked)

        # Left Button
        btn_left = QPushButton(self)
        btn_left.setIcon(QIcon("buttons/btn_left.png"))
        btn_left.setFixedSize(100, 100)
        btn_left.setIconSize(btn_left.size())
        btn_left.setStyleSheet("border: none; padding: 0px;")
        btn_left.clicked.connect(self.on_leftBtn_clicked)

        # Left Button
        btn_rotate_left = QPushButton(self)
        btn_rotate_left.setIcon(QIcon("buttons/btn_rotate_left.png"))
        btn_rotate_left.setFixedSize(100, 100)
        btn_rotate_left.setIconSize(btn_rotate_left.size())
        btn_rotate_left.setStyleSheet("border: none; padding: 0px;")
        btn_rotate_left.clicked.connect(self.on_btn_rotate_left_clicked)

        # Right Button
        btn_rotate_right = QPushButton(self)
        btn_rotate_right.setIcon(QIcon("buttons/btn_rotate_right.png"))
        btn_rotate_right.setFixedSize(100, 100)
        btn_rotate_right.setIconSize(btn_rotate_right.size())
        btn_rotate_right.setStyleSheet("border: none; padding: 0px;")
        btn_rotate_right.clicked.connect(self.on_btn_rotate_right_clicked)

        # Dominance Dance Button
        btn_dominance_dance = QPushButton(self)
        btn_dominance_dance.setIcon(QIcon("buttons/btn_dominance_dance.png"))
        btn_dominance_dance.setFixedSize(100, 100)
        btn_dominance_dance.setIconSize(btn_dominance_dance.size())
        btn_dominance_dance.setStyleSheet("border: none; padding: 0px;")
        btn_dominance_dance.clicked.connect(self.on_btn_dominance_dance_clicked)

        # Circle Dance Button
        btn_circle_dance = QPushButton(self)
        btn_circle_dance.setIcon(QIcon("buttons/btn_circle_dance.png"))
        btn_circle_dance.setFixedSize(100, 100)
        btn_circle_dance.setIconSize(btn_circle_dance.size())
        btn_circle_dance.setStyleSheet("border: none; padding: 0px;")
        btn_circle_dance.clicked.connect(self.on_btn_circle_dance_clicked)

        # Switch Mode Button
        self.btn_switch_mode = QPushButton(self)
        self.btn_switch_mode.setGeometry(10, 10, 100, 100)
        self.btn_switch_mode.setStyleSheet("border: none; padding: 0px;")
        self.btn_switch_mode.clicked.connect(self.on_btn_switch_mode_clicked)
        self.update_switch_icon()

        # Crosse all cases Button
        btn_cross_all_cases = QPushButton(self)
        btn_cross_all_cases.setIcon(QIcon("buttons/btn_cross_all_cases.png"))
        btn_cross_all_cases.setGeometry(400, 610, 100, 100)
        btn_cross_all_cases.setIconSize(btn_cross_all_cases.size())
        btn_cross_all_cases.setStyleSheet("border: none; padding: 0px;")
        btn_cross_all_cases.clicked.connect(self.on_btn_cross_all_cases_clicked)

        self.label = QLabel(self)
        pixmap = QPixmap("image/track.png")
        self.label.setGeometry(QRect(100, 10, 800, 80))
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)

        # Create grid layout
        grid_moves = QGridLayout()
        grid_moves.addWidget(btn_forward, 0, 1)
        grid_moves.addWidget(btn_right, 1, 2)
        grid_moves.addWidget(btn_backward, 2, 1)
        grid_moves.addWidget(btn_left, 1, 0)
        grid_moves.addWidget(btn_rotate_left, 0, 0)
        grid_moves.addWidget(btn_rotate_right, 0, 2)

        # Create grid layout
        grid_dances = QGridLayout()
        grid_dances.addWidget(btn_dominance_dance, 0, 0)
        grid_dances.addWidget(btn_circle_dance, 0, 1)

        # Add container to resize grid_moves
        container_moves = QWidget(self)
        container_moves.setLayout(grid_moves)
        container_moves.setGeometry(0, 320, 400, 400) # x, y, width, height

        # Add container to resize grid_dances
        container_dances = QWidget(self)
        container_dances.setLayout(grid_dances)
        container_dances.setGeometry(400, 520, 400, 100) # x, y, width, height

    def on_forwardBtn_clicked(self):
        if not (self.list_mode):
            print("Forward !")
            if not self.moves.marty.is_moving():
                self.moves.walkcase(1, "forward")

    def on_rightBtn_clicked(self):
        if not (self.list_mode):
            print("Right !")
            if not self.moves.marty.is_moving():
                self.moves.sidecase(1, "right")

    def on_backwardBtn_clicked(self):
        if not (self.list_mode):
            print("Backward !")
            if not self.moves.marty.is_moving():
                self.moves.walkcase(1, "backward")

    def on_leftBtn_clicked(self):
        if not (self.list_mode):
            print("Left !")
            if not self.moves.marty.is_moving():
                self.moves.sidecase(1, "left")

    def on_btn_rotate_left_clicked(self):
        if not (self.list_mode):
            print("Rotate Left !")
            if not self.moves.marty.is_moving():
                self.moves.turn("left")

    def on_btn_rotate_right_clicked(self):
        if not (self.list_mode):
            print("Rotate Right !")
            if not self.moves.marty.is_moving():
                self.moves.turn("right")

    def on_btn_dominance_dance_clicked(self):
        if not (self.list_mode):
            print("Dominance Dance !")
            if not self.moves.marty.is_moving():
                self.moves.circletime(1)

    def on_btn_circle_dance_clicked(self):
        if not (self.list_mode):
            print("Circle Dance !")
            if not self.moves.marty.is_moving():
                self.moves.circletime(3)

    def update_switch_icon(self):
        if self.list_mode:
            icon_path = "buttons/btn_switch_mode2.png"
        else:
            icon_path = "buttons/btn_switch_mode1.png"

        self.btn_switch_mode.setIcon(QIcon(icon_path))
        self.btn_switch_mode.setIconSize(self.btn_switch_mode.size())
        self.btn_switch_mode.setStyleSheet("border: none; padding: 0px;")
    
    def on_btn_switch_mode_clicked(self):
        self.list_mode = not self.list_mode
        self.update_switch_icon()

    def on_btn_cross_all_cases_clicked(self):
        if not (self.list_mode):
            self.moves.calibration_path()

    def keyPressEvent(self, event):
        if self.list_mode or self.moves.marty.is_moving():
            return

        key = event.key()
        if key == Qt.Key_Z:
            print("Key Z - Forward")
            self.on_forwardBtn_clicked()
        elif key == Qt.Key_S:
            print("Key S - Backward")
            self.on_backwardBtn_clicked()
        elif key == Qt.Key_Q:
            print("Key Q - Left")
            self.on_leftBtn_clicked()
        elif key == Qt.Key_D:
            print("Key D - Right")
            self.on_rightBtn_clicked()
        elif key == Qt.Key_A:
            print("Key A - Rotate Left")
            self.on_btn_rotate_left_clicked()
        elif key == Qt.Key_E:
            print("Key E - Rotate Right")
            self.on_btn_rotate_right_clicked()
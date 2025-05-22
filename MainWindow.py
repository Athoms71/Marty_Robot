from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, moves):
        super().__init__()
        self.setWindowTitle("Optimus Prime")
        self.resize(1280, 720)

        self.moves = moves
        self.list_mode = False

        # Forward Button
        btn_forward = QPushButton(self)
        btn_forward.setIcon(QIcon("buttons/btn_forward.png"))
        btn_forward.setFixedSize(100, 100)
        btn_forward.clicked.connect(self.on_forwardBtn_clicked)

        # right Button
        btn_right = QPushButton(self)
        btn_right.setIcon(QIcon("buttons/btn_right.png"))
        btn_right.setFixedSize(100, 100)
        btn_right.clicked.connect(self.on_rightBtn_clicked)

        # backward Button
        btn_backward = QPushButton(self)
        btn_backward.setIcon(QIcon("buttons/btn_backward.png"))
        btn_backward.setFixedSize(100, 100)
        btn_backward.clicked.connect(self.on_backwardBtn_clicked)

        # Left Button
        btn_left = QPushButton(self)
        btn_left.setIcon(QIcon("buttons/btn_left.png"))
        btn_left.setFixedSize(100, 100)
        btn_left.clicked.connect(self.on_leftBtn_clicked)

        # Left Button
        btn_rotate_left = QPushButton(self)
        btn_rotate_left.setIcon(QIcon("buttons/btn_rotate_left.png"))
        btn_rotate_left.setFixedSize(100, 100)
        btn_rotate_left.clicked.connect(self.on_btn_rotate_left_clicked)

        # Right Button
        btn_rotate_right = QPushButton(self)
        btn_rotate_right.setIcon(QIcon("buttons/btn_rotate_right.png"))
        btn_rotate_right.setFixedSize(100, 100)
        btn_rotate_right.clicked.connect(self.on_btn_rotate_right_clicked)

        # Classic Dance Button
        btn_classic_dance = QPushButton(self)
        btn_classic_dance.setIcon(QIcon("buttons/btn_classic_dance.png"))
        btn_classic_dance.setFixedSize(100, 100)
        btn_classic_dance.clicked.connect(self.on_btn_classic_dance_clicked)

        # Celebrate Dance Button
        btn_celebrate_dance = QPushButton(self)
        btn_celebrate_dance.setIcon(QIcon("buttons/btn_celebrate_dance.png"))
        btn_celebrate_dance.setFixedSize(100, 100)
        btn_celebrate_dance.clicked.connect(self.on_btn_celebrate_dance_clicked)

        # Circle Dance Button
        btn_circle_dance = QPushButton(self)
        btn_circle_dance.setIcon(QIcon("buttons/btn_circle_dance.png"))
        btn_circle_dance.setFixedSize(100, 100)
        btn_circle_dance.clicked.connect(self.on_btn_circle_dance_clicked)

        # Switch Mode Button
        btn_switch_mode = QPushButton(self)
        btn_switch_mode.setIcon(QIcon("buttons/btn_switch_mode1.png"))
        btn_switch_mode.setFixedSize(100, 100)
        btn_switch_mode.clicked.connect(self.on_btn_switch_mode_clicked)

        # Create grid layout
        grid_moves = QGridLayout()
        # Place buttons in grid
        grid_moves.addWidget(btn_forward, 0, 1)
        grid_moves.addWidget(btn_right, 1, 2)
        grid_moves.addWidget(btn_backward, 2, 1)
        grid_moves.addWidget(btn_left, 1, 0)
        grid_moves.addWidget(btn_rotate_left, 0, 0)
        grid_moves.addWidget(btn_rotate_right, 0, 2)

        # Create grid layout
        grid_dances = QGridLayout()
        grid_dances.addWidget(btn_classic_dance, 0, 0)
        grid_dances.addWidget(btn_celebrate_dance, 0, 1)
        grid_dances.addWidget(btn_circle_dance, 0, 2)

        # Add container to resize grid_moves
        container_moves = QWidget(self)
        container_moves.setLayout(grid_moves)
        container_moves.setGeometry(0, 300, 400, 400) # x, y, width, height

        # Add container to resize grid_dances
        container_dances = QWidget(self)
        container_dances.setLayout(grid_dances)
        container_dances.setGeometry(500, 300, 400, 400) # x, y, width, height

    def on_forwardBtn_clicked(self):
        print("Forward !")
        if not self.moves.marty.is_moving():
            self.moves.walk(num_steps=2, start_foot='auto', turn=0, step_length=25, move_time=1500)

    def on_rightBtn_clicked(self):
        print("Right !")
        if not self.moves.marty.is_moving():
            self.moves.sidestep(side="right", steps=2, step_length=35, move_time=1000, blocking=True)

    def on_backwardBtn_clicked(self):
        print("Backward !")
        if not self.moves.marty.is_moving():
            self.moves.walk(num_steps=2, start_foot='auto', turn=0, step_length=-25, move_time=1500)

    def on_leftBtn_clicked(self):
        print("Left !")
        if not self.moves.marty.is_moving():
            self.moves.sidestep(side="left", steps=2, step_length=35, move_time=1000, blocking=True)

    def on_btn_rotate_left_clicked(self):
        print("Rotate Left !")
        if not self.moves.marty.is_moving():
            self.moves.arms(left_angle=0, right_angle=135, move_time=1000, blocking=False)

            self.moves.walk(num_steps=1, start_foot='left', turn=0, step_length=-15, move_time=1500)
            self.moves.walk(num_steps=1, start_foot='right', turn=30, step_length=0, move_time=1500)
            self.moves.walk(num_steps=1, start_foot='left', turn=0, step_length=0, move_time=1500)

            self.moves.arms(left_angle=0, right_angle=0, move_time=1000, blocking=False)

    def on_btn_rotate_right_clicked(self):
        print("Rotate Right !")
        if not self.moves.marty.is_moving():
            self.moves.arms(left_angle=0, right_angle=135, move_time=1000, blocking=False)

            self.moves.walk(num_steps=1, start_foot='right', turn=0, step_length=-15, move_time=1500)
            self.moves.walk(num_steps=1, start_foot='left', turn=-30, step_length=0, move_time=1500)
            self.moves.walk(num_steps=1, start_foot='right', turn=0, step_length=0, move_time=1500)

            self.moves.arms(left_angle=0, right_angle=0, move_time=1000, blocking=False)

    def on_btn_classic_dance_clicked(self):
        print("Classic Dance !")
        if not self.moves.marty.is_moving():
            self.moves.dance()

    def on_btn_celebrate_dance_clicked(self):
        print("Celebrate Dance !")
        if not self.moves.marty.is_moving():
            self.moves.dance()

    def on_btn_circle_dance_clicked(self):
        print("Circle Dance !")
        if not self.moves.marty.is_moving():
            self.moves.dance()

    def on_btn_switch_mode_clicked(self):
        if (self.list_mode):
            self.btn_switch_mode.setIcon(QIcon("buttons/btn_switch_mode1.png"))
            self.list_mode = False

        else:
            self.btn_switch_mode.setIcon(QIcon("buttons/btn_switch_mode2.png"))
            self.list_mode = True

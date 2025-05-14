from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, moves):
        super().__init__()
        self.moves = moves
        self.setWindowTitle("Optimus Prime")
        self.resize(1280, 720)

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

        # Create grid layout
        gridButtons = QGridLayout()
        # Place buttons in grid
        gridButtons.addWidget(btn_forward, 0, 1)
        gridButtons.addWidget(btn_right, 1, 2)
        gridButtons.addWidget(btn_backward, 2, 1)
        gridButtons.addWidget(btn_left, 1, 0)
        gridButtons.addWidget(btn_rotate_left, 0, 0)
        gridButtons.addWidget(btn_rotate_right, 0, 2)


        # Add container to resize gridButtons
        container = QWidget(self)
        container.setLayout(gridButtons)
        container.setGeometry(0, 300, 400, 400) # x, y, width, height

    def on_forwardBtn_clicked(self):
        print("Forward !")
        self.moves.walk_forward(num_steps=2, start_foot='auto', turn=0, step_length=25, move_time=1500)

    def on_rightBtn_clicked(self):
        print("Right !")

    def on_backwardBtn_clicked(self):
        print("Backward !")

    def on_leftBtn_clicked(self):
        print("Left !")

    def on_btn_rotate_left_clicked(self):
        print("Rotate Left !")

    def on_btn_rotate_right_clicked(self):
        print("Rotate Right !")
    
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QGridLayout
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Marty Robot")
        self.resize(1280, 720)

        # Forward Button
        btn_forward = QPushButton(self)
        btn_forward.setIcon(QIcon("buttons/btn_forward.png"))
        btn_forward.setFixedSize(100, 100)

        # right Button
        btn_right = QPushButton(self)
        btn_right.setIcon(QIcon("buttons/btn_right.png"))
        btn_right.setFixedSize(100, 100)

        # backward Button
        btn_backward = QPushButton(self)
        btn_backward.setIcon(QIcon("buttons/btn_backward.png"))
        btn_backward.setFixedSize(100, 100)

        # Left Button
        btn_left = QPushButton(self)
        btn_left.setIcon(QIcon("buttons/btn_left.png"))
        btn_left.setFixedSize(100, 100)

        # Create grid layout
        gridButtons = QGridLayout()
        # Place buttons in grid
        gridButtons.addWidget(btn_forward, 0, 1)
        gridButtons.addWidget(btn_right, 1, 2)
        gridButtons.addWidget(btn_backward, 2, 1)
        gridButtons.addWidget(btn_left, 1, 0)

        # Add container to resize gridButtons
        container = QWidget(self)
        container.setLayout(gridButtons)
        container.setGeometry(0, 300, 400, 400) # x, y, width, height

        # Connect click signal
        btn_forward.clicked.connect(self.on_forwardBtn_clicked)
        btn_right.clicked.connect(self.on_rightBtn_clicked)
        btn_backward.clicked.connect(self.on_backwardBtn_clicked)
        btn_left.clicked.connect(self.on_leftBtn_clicked)

    def on_forwardBtn_clicked(self):
        print("Forward !")

    def on_rightBtn_clicked(self):
        print("Right !")

    def on_backwardBtn_clicked(self):
        print("Backward !")

    def on_leftBtn_clicked(self):
        print("Left !")

    
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt, QRect
import os

def resource_path(*paths):
    # Retourne le chemin absolu
    base = os.path.dirname(__file__)
    return os.path.join(base, *paths)

class MainWindow(QWidget):
    def __init__(self, moves):
        super().__init__()
        self.setWindowTitle("Optimus Prime")
        self.resize(1280, 720)

        self.mode = 0   # 0 = normal, 1 = list mode, 2 = mouse mode
        self.moves = moves

        # Background Image
        palette = QPalette()
        bg_path = resource_path('image', 'background.jpg')
        bg_pix = QPixmap(bg_path)
        palette.setBrush(QPalette.Window, QBrush(bg_pix.scaled(self.size(), Qt.KeepAspectRatioByExpanding)))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Track Image
        self.label = QLabel(self)
        track_path = resource_path('image', 'track.png')
        track_pix = QPixmap(track_path)
        self.label.setPixmap(track_pix)
        self.label.setScaledContents(True)
        self.label.setGeometry(500, 600, 750, 100)

        # Créer tous les boutons de base
        def make_button(icon_file, function):
            btn = QPushButton(self)
            path = resource_path('buttons', icon_file)
            ic = QIcon(path)
            btn.setIcon(ic)
            btn.setFixedSize(100, 100)
            btn.setIconSize(btn.size())
            btn.setStyleSheet("border: none; padding: 0px;")
            btn.clicked.connect(function)
            return btn

        btn_forward = make_button('btn_forward.png', self.on_btn_forward_clicked)
        btn_right = make_button('btn_right.png', self.on_btn_right_clicked)
        btn_backward = make_button('btn_backward.png', self.on_btn_backward_clicked)
        btn_left = make_button('btn_left.png', self.on_btn_left_clicked)
        btn_rotate_left = make_button('btn_rotate_left.png', self.on_btn_rotate_left_clicked)
        btn_rotate_right = make_button('btn_rotate_right.png', self.on_btn_rotate_right_clicked)

        btn_dominance_dance = make_button('btn_dominance_dance.png', self.on_btn_dominance_dance_clicked)
        btn_circle_dance = make_button('btn_circle_dance.jpg', self.on_btn_circle_dance_clicked)

        btn_calibrate = make_button('btn_calibrate.png', self.on_btn_calibrate_clicked)

        btn_start_sequencial = make_button('btn_start_sequential.png', self.on_btn_start_sequential_clicked)
        btn_save_sequencial = make_button('btn_save_sequential.png', self.on_btn_save_sequential_clicked)
        btn_load_sequencial = make_button('btn_load_sequential.png', self.on_btn_load_sequential_clicked)

        # Boutons de mode stockés comme attributs
        self.btn_normal_mode = QPushButton(self)
        self.btn_normal_mode.setFixedSize(100, 100)
        self.btn_normal_mode.clicked.connect(self.on_btn_normal_mode_clicked)

        self.btn_sequential_mode = QPushButton(self)
        self.btn_sequential_mode.setFixedSize(100, 100)
        self.btn_sequential_mode.clicked.connect(self.on_btn_sequential_mode_clicked)

        self.btn_mouse_mode = QPushButton(self)
        self.btn_mouse_mode.setFixedSize(100, 100)
        self.btn_mouse_mode.clicked.connect(self.on_btn_mouse_mode_clicked)

        # Dictionnaire pour mise à jour des icônes
        self.mode_buttons = {
            0: self.btn_normal_mode,
            1: self.btn_sequential_mode,
            2: self.btn_mouse_mode
        }
        # Initialise les icônes de mode
        self.update_icon_modes()

        # Layouts
        grid_moves = QGridLayout()
        grid_moves.addWidget(btn_forward, 0, 1)
        grid_moves.addWidget(btn_right, 1, 2)
        grid_moves.addWidget(btn_backward, 2, 1)
        grid_moves.addWidget(btn_left, 1, 0)
        grid_moves.addWidget(btn_rotate_left, 0, 0)
        grid_moves.addWidget(btn_rotate_right, 0, 2)

        grid_dances = QGridLayout()
        grid_dances.addWidget(btn_dominance_dance, 0, 0)
        grid_dances.addWidget(btn_circle_dance, 0, 1)

        grid_modes = QGridLayout()
        grid_modes.addWidget(self.btn_normal_mode, 0, 0)
        grid_modes.addWidget(self.btn_sequential_mode, 0, 1)
        grid_modes.addWidget(self.btn_mouse_mode, 0, 2)

        grid_other = QGridLayout()
        grid_other.addWidget(btn_calibrate, 0, 0)

        grid_sequential = QGridLayout()
        grid_sequential.addWidget(btn_start_sequencial, 0, 0)
        grid_sequential.addWidget(btn_save_sequencial, 0, 1)
        grid_sequential.addWidget(btn_load_sequencial, 0, 2)

        # Containers
        container_moves = QWidget(self)
        container_moves.setLayout(grid_moves)
        container_moves.setGeometry(0, 320, 400, 400)

        container_dances = QWidget(self)
        container_dances.setLayout(grid_dances)
        container_dances.setGeometry(10, 200, 240, 120)

        container_modes = QWidget(self)
        container_modes.setLayout(grid_modes)
        container_modes.setGeometry(10, 10, 400, 120)

        container_other = QWidget(self)
        container_other.setLayout(grid_other)
        container_other.setGeometry(800, 10, 200, 200)

        container_sequential = QWidget(self)
        container_sequential.setLayout(grid_sequential)
        container_sequential.setGeometry(500, 450, 400, 120)

    def update_icon_modes(self):
        names = ['normal', 'sequential', 'mouse']
        for idx, btn in self.mode_buttons.items():
            suffix = '2' if idx == self.mode else '1'
            icon_path = resource_path('buttons', f'btn_{names[idx]}_mode{suffix}.png')
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(btn.size())
            btn.setStyleSheet("border: none; padding: 0px;")


    def on_btn_normal_mode_clicked(self):
        self.mode = 0
        self.update_icon_modes()

    def on_btn_sequential_mode_clicked(self):
        self.mode = 1
        self.update_icon_modes()

    def on_btn_mouse_mode_clicked(self):
        self.mode = 2
        self.update_icon_modes()


    def on_btn_forward_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.walkcase(1, "forward")

    def on_btn_right_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.sidecase(1, "right")

    def on_btn_backward_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.walkcase(1, "backward")

    def on_btn_left_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.sidecase(1, "left")

    def on_btn_rotate_left_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.turn("left")

    def on_btn_rotate_right_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.turn("right")

    def on_btn_dominance_dance_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.circletime(1)

    def on_btn_circle_dance_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.circletime(3)

    def on_btn_calibrate_clicked(self):
        pass

    def on_btn_start_sequential_clicked(self):
        pass

    def on_btn_save_sequential_clicked(self):
        pass

    def on_btn_load_sequential_clicked(self):
        pass
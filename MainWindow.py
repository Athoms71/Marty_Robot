from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt, QTimer
import os
from MouseTrackingWindow import MouseTrackingWindow
from AbsoluteWindow import AbsoluteWindow


class MainWindow(QWidget):
    def __init__(self, moves, sequential, capteur):
        super().__init__()
        self.setWindowTitle("Optimus Prime")
        self.resize(1280, 720)

        self.moves = moves
        self.capteur = capteur

        self.sequential = sequential
        self.absolute_window = None     # Pour la fenêtre de parcours absolu
        self.mouse_tracking_window = None # Pour la fenêtre de suivi de la souris

        self.mode = 0                   # 0 = normal, 1 = seq mode, 2 = abs mode, 3 = mouse mode
        self.sequence_file_name = ""    # Nom du fichier pour sauvegarder/charger la SEQ ou ABS
        self.grid_size = 3              # Taille de la grille par défaut
        self.base_path = os.path.dirname(__file__)

        # Background Image
        palette = QPalette()
        bg_path = os.path.join(self.base_path, 'image', 'background.jpg')
        bg_pix = QPixmap(bg_path)
        palette.setBrush(QPalette.Window, QBrush(bg_pix.scaled(self.size(), Qt.KeepAspectRatioByExpanding)))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Track Image
        self.label = QLabel(self)
        track_path = os.path.join(self.base_path, 'image', 'track.png')
        track_pix = QPixmap(track_path)
        self.label.setPixmap(track_pix)
        self.label.setScaledContents(True)
        self.label.setGeometry(450, 450, 810, 255)

        # Battery Label
        self.battery_label = QLabel(self)
        self.battery_label.setStyleSheet("color: white; font-size: 16px; background-color: rgba(0, 0, 0, 100);")
        self.battery_label.setGeometry(1100, 10, 150, 30)

        # Position Label
        self.position_label = QLabel(self)
        self.position_label.setStyleSheet("color: white; font-size: 16px; background-color: rgba(0, 0, 0, 100);")
        self.position_label.setGeometry(1100, 50, 150, 30)

        # Distance Label
        self.distance_label = QLabel(self)
        self.distance_label.setStyleSheet("color: white; font-size: 16px; background-color: rgba(0, 0, 0, 100);")
        self.distance_label.setGeometry(1100, 90, 150, 30)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_battery)
        self.timer.timeout.connect(self.update_position)
        self.timer.timeout.connect(self.update_distance)
        self.timer.start(500)

        # Préchargement des icônes de track
        self.track_icons = {
            'U': QPixmap(os.path.join(self.base_path, 'buttons', 'btn_forward.png')),
            'R': QPixmap(os.path.join(self.base_path, 'buttons', 'btn_right.png')),
            'B': QPixmap(os.path.join(self.base_path, 'buttons', 'btn_backward.png')),
            'L': QPixmap(os.path.join(self.base_path, 'buttons', 'btn_left.png')),
        }

        # Liste pour garder une trace des QLabel utilisés pour le track
        self.track_labels = []

        # Créer tous les boutons de base
        def make_button(icon_file, size, function):
            btn = QPushButton(self)
            path = os.path.join(self.base_path, 'buttons', icon_file)
            ic = QIcon(path)
            btn.setIcon(ic)
            btn.setFixedSize(size, size)
            btn.setIconSize(btn.size())
            btn.setStyleSheet("border: none; padding: 0px;")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(function)
            return btn

        btn_forward = make_button('btn_forward.png', 100, self.on_btn_forward_clicked)
        btn_right = make_button('btn_right.png', 100, self.on_btn_right_clicked)
        btn_backward = make_button('btn_backward.png', 100, self.on_btn_backward_clicked)
        btn_left = make_button('btn_left.png', 100, self.on_btn_left_clicked)
        btn_rotate_left = make_button('btn_rotate_left.png', 100, self.on_btn_rotate_left_clicked)
        btn_rotate_right = make_button('btn_rotate_right.png', 100, self.on_btn_rotate_right_clicked)
        btn_right_arm = make_button('btn_right_arm.png', 100, self.on_btn_right_arm_clicked)
        btn_left_arm = make_button('btn_left_arm.png', 100, self.on_btn_left_arm_clicked)
        btn_origin = make_button('btn_origin.png', 100, self.on_btn_origin_clicked)

        btn_dominance_dance = make_button('btn_dominance_dance.png', 100, self.on_btn_dominance_dance_clicked)
        btn_circle_dance = make_button('btn_circle_dance.jpg', 100, self.on_btn_circle_dance_clicked)

        btn_calibrate = make_button('btn_calibrate.png', 100, self.on_btn_calibrate_clicked)

        btn_start_sequencial = make_button('btn_start_sequential.png', 80, self.on_btn_start_sequential_clicked)
        btn_save_sequencial = make_button('btn_save_sequential.png', 80, self.on_btn_save_sequential_clicked)
        btn_load_sequencial = make_button('btn_load_sequential.png', 80, self.on_btn_load_sequential_clicked)
        btn_clear_sequencial = make_button('btn_clear_sequential.png', 80, self.on_btn_clear_sequential_clicked)

        # Boutons de mode stockés comme attributs
        btn_normal_mode = make_button('btn_normal_mode1.png', 100, self.on_btn_normal_mode_clicked)
        btn_sequential_mode = make_button('btn_sequential_mode1.png', 100, self.on_btn_sequential_mode_clicked)
        btn_absolute_mode = make_button('btn_absolute_mode1.png', 100, self.on_btn_absolute_mode_clicked)
        btn_mouse_mode = make_button('btn_mouse_mode1.png', 100, self.on_btn_mouse_mode_clicked)

        # Champ de saisie pour le nom du fichier
        input_file_name = QLineEdit(self)
        input_file_name.setPlaceholderText("File name for save/load")
        input_file_name.setFixedSize(200, 40)
        input_file_name.setStyleSheet("background-color: white; font-size: 14px; padding: 2px;")
        input_file_name.textChanged.connect(self.on_input_file_name_changed)

        # Champ de saisie pour la taille de la grille
        input_grid_size = QLineEdit(self)
        input_grid_size.setPlaceholderText("Grid Size (3, 5, or 7)")
        input_grid_size.setGeometry(700, 50, 150, 40)
        input_grid_size.setStyleSheet("background-color: white; font-size: 14px; padding: 2px;")
        input_grid_size.textChanged.connect(self.on_input_grid_size_changed)

        # Dictionnaire pour mise à jour des icônes
        self.mode_buttons = {
            0: btn_normal_mode,
            1: btn_sequential_mode,
            2: btn_absolute_mode,
            3: btn_mouse_mode
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
        grid_moves.addWidget(btn_right_arm, 2, 2)
        grid_moves.addWidget(btn_left_arm, 2, 0)
        grid_moves.addWidget(btn_origin, 1, 1)

        grid_dances = QGridLayout()
        grid_dances.addWidget(btn_dominance_dance, 0, 0)
        grid_dances.addWidget(btn_circle_dance, 0, 1)

        grid_other = QGridLayout()
        grid_other.addWidget(btn_calibrate, 0, 0)

        grid_sequential = QGridLayout()
        grid_sequential.addWidget(btn_start_sequencial, 1, 0)
        grid_sequential.addWidget(btn_clear_sequencial, 0, 1)
        grid_sequential.addWidget(btn_save_sequencial, 0, 2)
        grid_sequential.addWidget(btn_load_sequencial, 0, 3)
        grid_sequential.addWidget(input_file_name, 0, 4)

        grid_modes = QGridLayout()
        grid_modes.addWidget(btn_normal_mode, 0, 0)
        grid_modes.addWidget(btn_sequential_mode, 0, 1)
        grid_modes.addWidget(btn_absolute_mode, 0, 2)
        grid_modes.addWidget(btn_mouse_mode, 0, 3)

        # Containers
        container_moves = QWidget(self)
        container_moves.setLayout(grid_moves)
        container_moves.setGeometry(0, 320, 400, 400)

        container_dances = QWidget(self)
        container_dances.setLayout(grid_dances)
        container_dances.setGeometry(10, 200, 240, 120)

        container_other = QWidget(self)
        container_other.setLayout(grid_other)
        container_other.setGeometry(900, 10, 120, 120)

        container_sequential = QWidget(self)
        container_sequential.setLayout(grid_sequential)
        container_sequential.setGeometry(405, 353, 700, 200)

        container_modes = QWidget(self)
        container_modes.setLayout(grid_modes)
        container_modes.setGeometry(10, 10, 400, 120)

    def update_icon_modes(self):
        names = ['normal', 'sequential', 'absolute', 'mouse']
        for idx, btn in self.mode_buttons.items():
            suffix = '2' if idx == self.mode else '1'
            icon_path = os.path.join(self.base_path, 'buttons', f'btn_{names[idx]}_mode{suffix}.png')
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(btn.size())
            btn.setStyleSheet("border: none; padding: 0px;")

    def update_icon_track(self):
        # Supprime les anciens labels
        for label in self.track_labels:
            label.setParent(None)
            label.deleteLater()
        self.track_labels.clear()

        moves = self.sequential.get_list_moves()  # [['1U'], ['2L'], ...]

        x_start = 515
        y_start = 465
        size = 56

        nb = 0
        for move in moves:  # Ignore la première ligne
            count = int(move[:-1])
            direction = move[-1]
            if direction in self.track_icons:
                for j in range(count):  # Répète l'icône selon le nombre
                    if nb < 13:
                        x_pos = x_start + nb * size
                        y_pos = y_start
                    if nb == 13:
                        x_pos = x_start + 12 * size
                        y_pos = y_start + size
                    if nb == 14:
                        x_pos = x_start + 12 * size
                        y_pos = y_start + 2 * size
                    if nb > 14:
                        x_pos = x_start + size * (27 - nb)
                        y_pos = y_start + 3 * size

                    label = QLabel(self)
                    label.setPixmap(self.track_icons[direction])
                    label.setGeometry(x_pos, y_pos, size, size)
                    label.setScaledContents(True)
                    label.show()
                    self.track_labels.append(label)
                    nb += 1

    def update_battery(self):
        self.battery_label.setText("Battery: " + str(self.capteur.get_battery()) + "%")

    def update_position(self):
        self.position_label.setText("Position: " + str(self.moves.pos))

    def update_distance(self):
        self.distance_label.setText("Distance: " + str(self.capteur.get_distance()))


    def on_btn_forward_clicked(self):
        if self.mode == 0:
            if self.moves.marty and not self.moves.marty.is_moving():
                self.moves.walkcase(1, "forward")
        elif self.mode == 1:
            self.sequential.add_move('1U')
            self.update_icon_track()

    def on_btn_right_clicked(self):
        if self.mode == 0:
            if self.moves.marty and not self.moves.marty.is_moving():
                self.moves.sidecase(1, "right")
        elif self.mode == 1:
            self.sequential.add_move('1R')
            self.update_icon_track()

    def on_btn_backward_clicked(self):
        if self.mode == 0:
            if self.moves.marty and not self.moves.marty.is_moving():
                self.moves.walkcase(1, "backward")
        elif self.mode == 1:
            self.sequential.add_move('1B')
            self.update_icon_track()

    def on_btn_left_clicked(self):
        if self.mode == 0:
            if self.moves.marty and not self.moves.marty.is_moving():
                self.moves.sidecase(1, "left")
        elif self.mode == 1:
            self.sequential.add_move('1L')
            self.update_icon_track()

    def on_btn_rotate_left_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.turn("left")

    def on_btn_rotate_right_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.turn("right")

    def on_btn_right_arm_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.get_marty().arms(left_angle=0, right_angle=135,
                                        move_time=500, blocking=True)
            self.moves.get_marty().arms(left_angle=0, right_angle=0,
                                        move_time=500, blocking=True)

    def on_btn_left_arm_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.get_marty().arms(left_angle=135, right_angle=0,
                                        move_time=500, blocking=True)
            self.moves.get_marty().arms(left_angle=0, right_angle=0,
                                        move_time=500, blocking=True)

    def on_btn_origin_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.go_to_origin(self.grid_size)


    def keyPressEvent(self, event):
        # Ne rien faire si le focus est sur un champ texte (comme QLineEdit)
        if isinstance(self.focusWidget(), QLineEdit):
            return
        
        if self.moves.marty and not self.moves.marty.is_moving():
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

    
    def on_btn_dominance_dance_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.circletime(1)

    def on_btn_circle_dance_clicked(self):
        if self.mode == 0 and self.moves.marty and not self.moves.marty.is_moving():
            self.moves.circletime(3)


    def on_btn_calibrate_clicked(self):
        self.moves.calibration_path(self.grid_size)

    def on_input_grid_size_changed(self, text):
        if text not in {"3", "5", "7"}:
            self.sender().setStyleSheet("background-color: #ffcccc;")  # rouge clair = invalide
        else:
            self.sender().setStyleSheet("background-color: white;")    # valide
            self.grid_size = int(text)


    def on_btn_start_sequential_clicked(self):
        if self.moves.marty and not self.moves.marty.is_moving():
            self.sequential.play_dance()

    def on_btn_clear_sequential_clicked(self):
        self.sequential.remove_move()
        self.update_icon_track()

    def on_btn_save_sequential_clicked(self):
        self.sequential.save_dance(self.sequence_file_name, self.grid_size)

    def on_btn_load_sequential_clicked(self):
        self.sequential.load_dance(self.sequence_file_name)
        self.update_icon_track()

    def on_input_file_name_changed(self, text):
        self.sequence_file_name = text


    def on_btn_normal_mode_clicked(self):
        self.mode = 0
        self.update_icon_modes()

    def on_btn_sequential_mode_clicked(self):
        self.mode = 1
        self.update_icon_modes()

    def on_btn_absolute_mode_clicked(self):
        self.mode = 2
        self.update_icon_modes()

        # Vérifie que la fenêtre n'existe pas
        if self.absolute_window is None:
            self.absolute_window = AbsoluteWindow(self.grid_size, self.sequence_file_name, self)
        else:
            self.absolute_window.show()
        
    def on_btn_mouse_mode_clicked(self):
        self.mode = 3
        self.update_icon_modes()

        # Vérifie que la fenêtre n'existe pas
        if self.mouse_tracking_window is None:
            self.mouse_tracking_window = MouseTrackingWindow(self.moves.marty, self)
        else:
            self.mouse_tracking_window.show()
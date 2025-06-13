from Moves import Moves
from martypy import Marty


class Sequential:
    def __init__(self, moves: Moves):
        self.moves = moves
        self.robot = moves.get_marty()
        self.list_moves = []
        self.dim = 'SEQ 3'

    def get_list_moves(self):
        return self.list_moves

    def add_move(self, move: str):
        """Ajoute un mouvement à list_moves, en incrémentant s’il est identique au précédent."""
        if len(self.list_moves) < 28:
            self.list_moves.append(move)

    def remove_move(self):
        """Supprime un mouvement de list_moves à l'index spécifié."""
        if len(self.list_moves) > 0:
            self.list_moves.pop(len(self.list_moves) - 1)

    def load_dance(self, file_path: str):
        """Charge le fichier .dance et stocke son contenu dans list_moves sous forme de liste 2D."""
        self.list_moves = []
        if file_path.endswith(".dance"):
            with open(file_path, "r") as fichier:
                lines = fichier.readlines()
                self.dim = lines[0]
                self.list_moves = []
                for line in lines[1:]:
                    if len(line) == 3:
                        self.list_moves.append(line.strip())
            print("Fichier chargé avec succès.")
        else:
            print("Le fichier est introuvable.")

    def save_dance(self, file_path: str):
        """Sauvegarde list_moves dans un fichier .dance, en format ligne par ligne."""
        if file_path.endswith(".dance"):
            with open(file_path, "w") as fichier:
                fichier.write(f"{self.dim}\n")
                for move in self.list_moves:
                    fichier.write(f"{move}\n")
            print("Fichier enregistré avec succès.")
        else:
            print("Le fichier est introuvable.")

    def check_edges(self, deplacement: list[int], dim: int):
        pos_x = self.moves.pos[0] + deplacement[0]
        pos_y = self.moves.pos[1] + deplacement[1]
        if (pos_x >= 0 and pos_x < dim) and (pos_y >= 0 and pos_y < dim):
            return True
        return False

    def play_dance(self):
        self.robot.pos = [(int(self.dim[4]) - 1)//2, (int(self.dim[4]) - 1)//2]

        if self.dim[:3] == "SEQ":
            for move in self.list_moves:
                count = int(move[0])
                direction = move[1]
                if direction == "U" and self.check_edges([0, -1], int(self.dim[4])):
                    self.moves.walkcase(count, "forward")
                elif direction == "B" and self.check_edges([0, 1], int(self.dim[4])):
                    self.moves.walkcase(count, "backward")
                elif direction == "R" and self.check_edges([1, 0], int(self.dim[4])):
                    self.moves.sidecase(count, "right")
                elif direction == "L" and self.check_edges([-1, 0], int(self.dim[4])):
                    self.moves.sidecase(count, "left")
        elif self.dim[:3] == "ABS":
            for move in self.list_moves:
                count = int(move[0])
                direction = move[1]
                if direction == "U" and self.check_edges([0, -count], int(self.dim[4])):
                    self.moves.walkcase(count, "forward")
                    self.robot.pos[1] -= count
                elif direction == "B" and self.check_edges([0, count], int(self.dim[4])):
                    self.moves.walkcase(count, "backward")
                    self.robot.pos[1] += count
                elif direction == "R" and self.check_edges([count, 0], int(self.dim[4])):
                    self.moves.sidecase(count, "right")
                    self.robot.pos[0] += count
                elif direction == "L" and self.check_edges([-count, 0], int(self.dim[4])):
                    self.moves.sidecase(count, "left")
                    self.robot.pos[0] -= count

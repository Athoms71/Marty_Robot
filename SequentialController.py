class Sequential:
    def __init__(self, moves):
        self.moves = moves
        self.robot = moves.get_marty()
        self.list_moves = []
   
    def load_dance(self, file_path: str):
        """Charge le fichier .dance et stocke son contenu dans list_moves sous forme de liste 2D."""
        if file_path.endswith(".dance"):
            with open(file_path, "r") as fichier:
                lines = fichier.readlines()
                self.list_moves = [line.strip().split() for line in lines[1:] if line.strip()]
            print("Fichier chargé avec succès.")
        else:
            print("Le fichier est introuvable.")

    def save_dance(self, file_path: str):
        """Sauvegarde list_moves dans un fichier .dance, en format ligne par ligne."""
        if file_path.endswith(".dance"):
            with open(file_path, "w") as fichier:
                fichier.write(f"SEQ {len(self.list_moves)}\n")
                for move in self.list_moves:
                    fichier.write(" ".join(move) + "\n")
            print("Fichier enregistré avec succès.")
        else:
            print("Le fichier est introuvable.")


    def get_list_moves(self):
        return self.list_moves

    def add_move(self, direction: str):
        """Ajoute un mouvement à list_moves, en incrémentant s’il est identique au précédent."""
        if self.list_moves and self.list_moves[-1][1] == direction:
            self.list_moves[-1][0] += 1
        else:
            self.list_moves.append([1, direction])

    def remove_move(self, index: int):
        """Supprime un mouvement de list_moves à l'index spécifié."""
        if 0 <= index < len(self.list_moves):
            self.list_moves.pop(index)


    def check_edges(self, deplacement: list[int], dim: int):
        pos_x = self.robot.pos[0] + deplacement[0]
        pos_y = self.robot.pos[1] + deplacement[1]
        if (pos_x >= 0 and pos_x < dim) and (pos_y >= 0 and pos_y < dim):
            return True
        return False

    def play_dance(self):
        """Lit les fichiers .dance en fonction de leur première ligne :\n- Si ABS : parcourt le chemin absolu depuis le centre de la grille\n- Si SEQ : parcourt le chemin relatif depuis la position de départ\n"""
        self.robot.pos = [(int(self.list_moves[0][4]) - 1)//2, (int(self.list_moves[0][4]) - 1)//2]

        if self.list_moves[0][:3] == "SEQ":
            for line in self.list_moves[1:]:
                line = line.split()[0]
                if line[1] == "U" and self.check_edges(self.robot, [0, -1], int(self.list_moves[0][4])):
                    self.moves.walkcase(int(line[0]))
                elif line[1] == "R" and self.check_edges(self.robot, [1, 0], int(self.list_moves[0][4])):
                    self.moves.sidecase(int(line[0]))
                elif line[1] == "L" and self.check_edges(self.robot, [-1, 0], int(self.list_moves[0][4])):
                    self.moves.sidecase(int(line[0]), "left")
                elif line[1] == "B" and self.check_edges(self.robot, [0, 1], int(self.list_moves[0][4])):
                    self.moves.walkcase(int(line[0]), "backward")
        elif self.list_moves[0][:-2] == "ABS":
            for line in self.list_moves[1:]:
                dy = int(line[1]) - self.robot.pos[1]
                dx = int(line[0]) - self.robot.pos[0]
                if dx < 0:
                    self.moves.sidecase(-dx)
                else:
                    self.moves.sidecase(dx, "left")
                if dy < 0:
                    self.moves.walkcase(-dy)
                else:
                    self.moves.walkcase(dy, "backward")
                self.robot.pos = [int(line[0]), int(line[1])]


    def go_to_origin(self, dim: int):
        dx = self.robot.pos[0] - (dim - 1)//2
        dy = self.robot.pos[1] - (dim - 1)//2
        if dx < 0:
            self.moves.sidecase(-dx)
        else:
            self.moves.sidecase(dx, "left")
        if dy < 0:
            self.moves.walkcase(-dy)
        else:
            self.moves.walkcase(dy, "backward")
        print("Le robot est actuellement au centre de la case")

from Moves import Moves
from martypy import Marty
import time


class Sequential:
    def __init__(self, moves: Moves):
        """
        Initialise la séquence avec un objet Moves.

        Args:
            moves (Moves): Instance de la classe Moves pour contrôler Marty.
        """
        self.moves = moves
        self.robot = moves.get_marty()
        # Liste des mouvements sous forme de chaînes (ex: "3U")
        self.list_moves = []
        # Format et dimension de la séquence (ex: 'SEQ 3')
        self.dim = 'SEQ 3'

    def get_list_moves(self) -> list[str]:
        """
        Retourne la liste actuelle des mouvements.

        Returns:
            list[str]: Liste des mouvements enregistrés.
        """
        return self.list_moves

    def add_move(self, move: str):
        """
        Ajoute un mouvement à la liste des mouvements si la taille est inférieure à 28.

        Args:
            move (str): Mouvement à ajouter (ex: "3U" pour 3 pas vers le haut).
        """
        if len(self.list_moves) < 28:
            self.list_moves.append(move)

    def remove_move(self):
        """
        Supprime le dernier mouvement ajouté dans la liste des mouvements.
        """
        if self.list_moves:
            self.list_moves.pop()

    def load_dance(self, file_path: str):
        """
        Charge une séquence de mouvements depuis un fichier .dance.

        Args:
            file_path (str): Chemin vers le fichier à charger.

        Note:
            Le fichier doit commencer par une ligne indiquant la dimension (ex: 'SEQ 3').
            Ensuite chaque ligne correspond à un mouvement (ex: '3U').
        """
        self.list_moves = []
        if file_path.endswith(".dance"):
            with open(file_path, "r") as fichier:
                lines = fichier.readlines()
                self.dim = lines[0].strip()
                self.list_moves = [line.strip()
                                   for line in lines[1:] if len(line.strip()) == 3]
            print("Fichier chargé avec succès.")
        else:
            print("Le fichier est introuvable.")

    def save_dance(self, file_path: str):
        """
        Sauvegarde la liste des mouvements dans un fichier .dance.

        Args:
            file_path (str): Chemin où enregistrer la séquence.

        Note:
            Le fichier est écrit uniquement si l'extension est '.dance'.
        """
        if file_path.endswith(".dance"):
            with open(file_path, "w") as fichier:
                fichier.write(f"{self.dim}\n")
                for move in self.list_moves:
                    fichier.write(f"{move}\n")
            print("Fichier enregistré avec succès.")
        else:
            print("Le fichier est introuvable.")

    def check_edges(self, deplacement: list[int], dim: int) -> bool:
        """
        Vérifie que le déplacement reste dans les limites de la grille.

        Args:
            deplacement (list[int]): Déplacement sous forme [dx, dy].
            dim (int): Dimension maximale autorisée.

        Returns:
            bool: True si le déplacement est valide, False sinon.
        """
        pos_x = self.moves.pos[0] + deplacement[0]
        pos_y = self.moves.pos[1] + deplacement[1]
        return 0 <= pos_x < dim and 0 <= pos_y < dim

    def play_dance(self):
        """
        Exécute la séquence de mouvements en contrôlant Marty.

        Gère les déplacements en mode séquentiel ('SEQ') ou absolu ('ABS'),
        en respectant les limites de la grille.

        Attend la fin de chaque mouvement avant de commencer le suivant.
        """
        center = (int(self.dim[4]) - 1) // 2
        self.moves.pos = [center, center]

        if self.dim.startswith("SEQ"):
            for move in self.list_moves:
                count = int(move[0])
                direction = move[1]
                if direction == "U" and self.check_edges([0, -count], int(self.dim[4])):
                    self.moves.walkcase(count, "forward")
                elif direction == "B" and self.check_edges([0, count], int(self.dim[4])):
                    self.moves.walkcase(count, "backward")
                elif direction == "R" and self.check_edges([count, 0], int(self.dim[4])):
                    self.moves.sidecase(count, "right")
                elif direction == "L" and self.check_edges([-count, 0], int(self.dim[4])):
                    self.moves.sidecase(count, "left")

                while self.robot.is_moving():
                    time.sleep(0.1)

        elif self.dim.startswith("ABS"):
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

                while self.robot.is_moving():
                    time.sleep(0.1)

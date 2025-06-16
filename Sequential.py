from Moves import Moves
from martypy import Marty
import time
import os


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
        # Dimension de la séquence (it will always write SEQ x)
        self.dim = 3

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
            self.list_moves.pop(-1)

    def convert_abs_to_seq(self, positions, start_pos):
        """
        Convertit une liste de positions absolues en une liste de mouvements séquentiels.

        Args:
            positions (list of tuple): Liste des positions (x, y) successives.

        Returns:
            list of str: Liste des mouvements au format SEQ (ex: '2U', '1R', etc.).
        """
        seq_moves = []
        positions = [start_pos]+positions
        for i in range(1, len(positions)):
            x0, y0 = positions[i - 1]
            x1, y1 = positions[i]

            dx = x1 - x0
            dy = y1 - y0

            # Convertir déplacement en mouvement SEQ
            if dx > 0:
                if dy > 0:
                    seq_moves.append(f"{dy}B")
                elif dy < 0:
                    seq_moves.append(f"{-dy}U")
                seq_moves.append(f"{dx}R")
            elif dx < 0:
                if dy > 0:
                    seq_moves.append(f"{dy}B")
                elif dy < 0:
                    seq_moves.append(f"{-dy}U")
                seq_moves.append(f"{-dx}L")
            elif dy > 0:
                seq_moves.append(f"{dy}B")  # Bas (Back)
            elif dy < 0:
                seq_moves.append(f"{-dy}U")  # Haut (Up)
        return seq_moves

    def load_dance(self, file_path: str):
        """
        Charge une séquence de mouvements depuis un fichier .dance.

        Args:
            file_path (str): Chemin vers le fichier à charger.
        """

        if not file_path.endswith(".dance"):
            print("Erreur : le fichier doit avoir l'extension .dance")
            return

        if not os.path.exists(file_path):
            print("Erreur : le fichier n'existe pas.")
            return

        try:
            with open(file_path, "r") as fichier:
                lines = fichier.readlines()

                if not lines:
                    print("Erreur : le fichier est vide.")
                    return

                self.list_moves = []  # Réinitialise la liste des mouvements
                header = lines[0].strip()
                moves_lines = [line.strip()
                               for line in lines[1:] if line.strip()]

                if header.startswith("SEQ"):
                    # Chargement direct
                    self.list_moves = moves_lines
                elif header.startswith("ABS"):
                    # Conversion des positions absolues en mouvements séquentiels
                    positions = [(int(move[1]), int(move[0]))
                                 for move in moves_lines]
                    self.list_moves = self.convert_abs_to_seq(
                        positions, self.moves.pos)
                else:
                    print("Format de fichier non reconnu.")
                    return

                print("Fichier chargé avec succès.")

        except Exception as e:
            print(f"Erreur lors du chargement du fichier : {e}")

    def save_dance(self, file_path: str, dim: int):
        """
        Sauvegarde la liste des mouvements dans un fichier .dance,
        en compressant les mouvements successifs ayant le même type (U, B, L, R).

        Args:
            file_path (str): Chemin où enregistrer la séquence.
            dim (int): Taille de la grille (ex: 3 pour SEQ 3).
        """
        if not file_path.endswith(".dance"):
            print("Erreur : l'extension du fichier doit être .dance")
            return

        try:
            self.dim = dim
            with open(file_path, "w") as fichier:
                fichier.write(f"SEQ {self.dim}\n")

                if not self.list_moves:
                    print("Aucun mouvement à sauvegarder.")
                    return

                # Initialisation avec le premier mouvement
                current_move = self.list_moves[0]
                current_count = int(current_move[:-1])  # Partie numérique
                current_dir = current_move[-1]  # Dernier caractère, ex: 'U'

                for move in self.list_moves[1:]:
                    direction = move[-1]
                    count = int(move[:-1])

                    if direction == current_dir:
                        current_count += count
                    else:
                        # Écrit le mouvement compressé
                        fichier.write(f"{current_count}{current_dir}\n")
                        # Réinitialise
                        current_dir = direction
                        current_count = count

                # Écrit le dernier mouvement
                fichier.write(f"{current_count}{current_dir}\n")

            print("Fichier enregistré avec succès.")
            print(self.list_moves)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du fichier : {e}")

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
        Exécute la séquence de mouvements définie dans `self.list_moves`.

        Chaque mouvement est de la forme "3U", "2L", etc., où :
            - Le chiffre indique le nombre de pas.
            - La lettre indique la direction : U (up), B (back), R (right), L (left).

        Le robot commence au centre de la grille SEQ. Avant chaque déplacement,
        les limites sont vérifiées. L'exécution attend que le robot termine
        un mouvement avant de passer au suivant.
        """
        center = (int(self.dim[4]) - 1) // 2
        self.moves.pos = (center, center)

        for move in self.list_moves:
            count = int(move[:-1])
            direction = move[-1]
            if direction == "U" and self.check_edges([0, -count], int(self.dim[4])):
                self.moves.walkcase(count, "forward")
            elif direction == "B" and self.check_edges([0, count], int(self.dim[4])):
                self.moves.walkcase(count, "backward")
            elif direction == "R" and self.check_edges([count, 0], int(self.dim[4])):
                self.moves.sidecase(count, "right")
            elif direction == "L" and self.check_edges([-count, 0], int(self.dim[4])):
                self.moves.sidecase(count, "left")

            time.sleep(10)

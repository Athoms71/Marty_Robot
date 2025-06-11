from Moves import Moves
from MartyController import MartyController


def play_dance(robot: MartyController, file_path: str):
    """Lit les fichiers .dance en fonction de leur première ligne :\n- Si ABS : parcourt le chemin absolu depuis le centre de la grille\n- Si SEQ : parcourt le chemin relatif depuis la position de départ\n"""
    if file_path[-6:] == ".dance":
        movement = Moves()
        fichier = open(file_path, "r")
        lines = fichier.readlines()
        robot.pos = [(int(lines[0][4])-1)//2, (int(lines[0][4])-1)//2]
        if lines[0][:3] == "SEQ":
            for line in lines[1:]:
                line = line.split()[0]
                if line[1] == "U":
                    movement.walkcase(int(line[0]))
                elif line[1] == "R":
                    movement.sidecase(int(line[0]))
                elif line[1] == "L":
                    movement.sidecase(int(line[0]), "left")
                elif line[1] == "B":
                    movement.walkcase(int(line[0]), "backward")
        elif lines[0][:-2] == "ABS":
            for line in lines[1:]:
                dy = int(line[1])-robot.pos[1]
                dx = int(line[0])-robot.pos[0]
                print(
                    f"Déplacement horizontal : {dx} / Déplacement vertical : {dy}")
                print(
                    f"Arrivée prévue en {robot.pos[0]+dx},{robot.pos[1]+dy} d'après les calculs")
                if dx < 0:
                    movement.sidecase(-dx)
                else:
                    movement.sidecase(dx, "left")
                if dy < 0:
                    movement.walkcase(-dy)
                else:
                    movement.walkcase(dy, "backward")
                robot.pos = [int(line[0]), int(line[1])]

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
                if line[1] == "U" and check_edges(robot, [0, -1], int(lines[0][4])):
                    movement.walkcase(int(line[0]))
                elif line[1] == "R" and check_edges(robot, [1, 0], int(lines[0][4])):
                    movement.sidecase(int(line[0]))
                elif line[1] == "L" and check_edges(robot, [-1, 0], int(lines[0][4])):
                    movement.sidecase(int(line[0]), "left")
                elif line[1] == "B" and check_edges(robot, [0, 1], int(lines[0][4])):
                    movement.walkcase(int(line[0]), "backward")
        elif lines[0][:-2] == "ABS":
            for line in lines[1:]:
                dy = int(line[1])-robot.pos[1]
                dx = int(line[0])-robot.pos[0]
                if dx < 0:
                    movement.sidecase(-dx)
                else:
                    movement.sidecase(dx, "left")
                if dy < 0:
                    movement.walkcase(-dy)
                else:
                    movement.walkcase(dy, "backward")
                robot.pos = [int(line[0]), int(line[1])]


def go_to_origin(robot: MartyController, dim: int):
    move = Moves()
    dx = robot.pos[0]-(dim-1)//2
    dy = robot.pos[1]-(dim-1)//2
    if dx < 0:
        move.sidecase(-dx)
    else:
        move.sidecase(dx, "left")
    if dy < 0:
        move.walkcase(-dy)
    else:
        move.walkcase(dy, "backward")
    print("Le robot est actuellement au centre de la case")


def check_edges(robot: MartyController, deplacement: list[int], dim: int):
    pos_x = robot.pos[0]+deplacement[0]
    pos_y = robot.pos[1]+deplacement[1]
    if (pos_x >= 0 and pos_x < dim) and (pos_y >= 0 and pos_y < dim):
        return True
    return False


play_dance(MartyController("wifi", "192.168.0.102"), "sequential.dance")

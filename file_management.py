def read_file(fichier: str):
    """Read the contents of a file and returns a dictionnary containing pairs 'color' : 'left'"""
    # Check if the file exists
    try:
        with open(fichier+".txt", 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {fichier} not found.")
    couleurs = []
    for line in lines:
        parts = line.strip().split(";")
        if len(parts) >= 2 and parts[0] and parts[1]:
            couleurs.append((parts[0], parts[1]))
    file.close()
    return couleurs


def read_file_hexatocolor(fichier: str,hexa:str):
    file= open(fichier+".txt", 'r')
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(";")
        if (parts[1]== hexa):
            return parts[0]

def read_mouv(fichier: str):
    try:
        with open(fichier, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {fichier} not found.")
        return

    # Vérifie si au moins une ligne contient un ';'
    if any(";" in line for line in lines):
        feel = []
        for line in lines:
            parts = line.strip().split(";")
            if len(parts) >= 3:
                feel.append([parts[0], parts[1], parts[2]])
        return feel
    else:
        dance = []
        for line in lines:
            dance.append(line.strip())
        return dance
    
def create_file(name: str, type: int):   # 0= dance, 1 = feel, 2 = couleur
    if type == 0:
        try:
            fichier = open(name + ".dance", 'w')
            fichier.close()
        except Exception as e:
            print(f"Failed to create file {name+ ".dance"}: {e}")
            return
    elif type == 1:
        try:
            fichier = open(name + ".feel", 'w')
            fichier.close()
        except Exception as e:
            print(f"Failed to create file {name+ ".feel"}: {e}")
            return
    elif type == 2:
        try:
            fichier = open(name + ".txt", 'w')
            fichier.close()
        except Exception as e:
            print(f"Failed to create file {name+ ".txt"}: {e}")
            return
    else:
        print("Type not recognized")
        return

def edit_feel_file(feel: list, filename: str = "new"):
    try:
        create_file(filename, 1)
        with open(f"{filename}.feel", 'a') as fichier:
            for action in feel:
                if len(action) == 3:
                    fichier.write(f'{action[0]};{action[1]};{action[2]}\n')
                else:
                    print(f"Action ignorée (format incorrect) : {action}")
        return True
    except Exception as e:
        print(f"Erreur lors de l'édition du fichier {filename}.feel : {e}")
        return False 
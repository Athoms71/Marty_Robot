def read_file(file_path: str):
    """Read the contents of a file and returns a dictionnary containing pairs 'color' : '[left,right]' or a tuple (left,right)."""
    # Check if the file exists
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    for line in lines:
        line = line.split(";")
        if (len(line) == 2):
            couleurs = (line[0], line[1])
        elif (len(line) == 3):
            couleurs[line[0]] = [int(line[1]), int(line[2])]
    return couleurs


def read_mouv(file_path: str):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
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
def read_file(fichier: str):
    """
    Lit un fichier texte et retourne une liste de tuples (couleur, position).

    Chaque ligne du fichier doit contenir deux valeurs séparées par un point-virgule.

    Args:
        fichier (str): Nom du fichier (sans extension .txt).

    Returns:
        list[tuple[str, str]]: Liste des paires (couleur, position).

    Note:
        Si le fichier n'existe pas, affiche un message d'erreur et retourne une liste vide.
    """
    try:
        with open(fichier + ".txt", 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {fichier} not found.")
        return []

    couleurs = []
    for line in lines:
        parts = line.strip().split(";")
        if len(parts) >= 2 and parts[0] and parts[1]:
            couleurs.append((parts[0], parts[1]))
    return couleurs


def read_file_hexatocolor(fichier: str, hexa: str):
    """
    Recherche la couleur associée à un code hexadécimal dans un fichier.

    Args:
        fichier (str): Nom du fichier (sans extension .txt).
        hexa (str): Code couleur hexadécimal à chercher (ex: "#ff0000").

    Returns:
        str|None: Nom de la couleur associée ou None si non trouvée.
    """
    try:
        with open(fichier + ".txt", 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {fichier} not found.")
        return None

    for line in lines:
        parts = line.strip().split(";")
        if len(parts) >= 2 and parts[1] == hexa:
            return parts[0]
    return None


def read_mouv(fichier: str):
    """
    Lit un fichier contenant soit des émotions soit une danse.

    Si le fichier contient des lignes avec ';', il retourne une liste d'émotions (listes de 3 éléments).
    Sinon, retourne une liste de mouvements (chaînes).

    Args:
        fichier (str): Chemin complet du fichier à lire.

    Returns:
        list: Liste des émotions (listes) ou mouvements (str), ou None si fichier non trouvé.
    """
    try:
        with open(fichier, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File {fichier} not found.")
        return None

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


def create_file(name: str, type: int):
    """
    Crée un fichier vide avec l'extension selon le type spécifié.

    Args:
        name (str): Nom du fichier sans extension.
        type (int): Type de fichier à créer:
                    0 = fichier .dance
                    1 = fichier .feel
                    2 = fichier .txt (couleurs)

    Note:
        Affiche un message d'erreur en cas d'échec.
    """
    extensions = {0: ".dance", 1: ".feel", 2: ".txt"}
    ext = extensions.get(type)
    if ext is None:
        print("Type not recognized")
        return

    try:
        with open(name + ext, 'w') as fichier:
            pass
    except Exception as e:
        print(f"Failed to create file {name + ext}: {e}")

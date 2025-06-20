from martypy import Marty
import time
import file_management as file_management


class Capteur:
    """
    Classe pour gérer les capteurs de Marty.

    Attributs:
        marty (Marty): instance du robot Marty.
    """

    def __init__(self, marty: Marty):
        """
        Initialise la classe Capteur avec une instance de Marty.
        """
        self.marty = marty

    def get_battery(self) -> int | None:
        """
        Récupère le niveau de batterie restant de Marty en pourcentage.

        Returns:
            int: Niveau de batterie (0-100), ou None si erreur.
        """
        try:
            return int(self.marty.get_battery_remaining())
        except Exception as e:
            print(f"Failed to read Marty battery level: {e}")
            return None

    def get_distance(self) -> float | None:
        """
        Récupère la valeur du capteur de distance de Marty.

        Returns:
            float: Distance détectée, ou None si erreur.
        """
        try:
            return float(self.marty.get_distance_sensor())
        except Exception as e:
            print(f"Failed to read Marty distance: {e}")
            return None

    @staticmethod
    def obstacle(marty: Marty):
        """
        Lit les valeurs des capteurs d'obstacles à droite et à gauche.

        Args:
            marty (Marty): instance de Marty.

        Affiche les valeurs des capteurs d'obstacles.
        """
        try:
            obstacle_right = float(marty.get_obstacle_sensor_reading("right"))
            obstacle_left = float(marty.get_obstacle_sensor_reading("left"))
        except Exception as e:
            print(f"Failed to read Marty obstacle: {e}")
            return

        print(f"Valeur obstacle droit: {obstacle_right}")
        print(f"Valeur obstacle gauche: {obstacle_left}")


def calibrate(marty: Marty, couleur: str, nom_fichier: str):
    """
    Enregistre la couleur détectée par les capteurs de Marty dans un fichier.

    Args:
        marty (Marty): instance du robot.
        couleur (str): nom ou code couleur à enregistrer.
        nom_fichier (str): nom du fichier sans extension.
    """
    try:
        with open(nom_fichier + '.txt', 'a') as fichier:
            hex_color = get_feet_colors_hex(marty)
            fichier.write(f"{couleur};{hex_color};\n")
    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier de calibration: {e}")


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    """
    Convertit un tuple RGB en chaîne hexadécimale.

    Args:
        rgb (tuple): tuple contenant les valeurs (R, G, B).

    Returns:
        str: code couleur hexadécimal.
    """
    return "{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))


def hexa_to_rgb(hexa: str):
    """
    Convertit une couleur hexadécimale en tuple RGB.
    """
    return tuple(int(hexa[i:i+2], 16) for i in (0, 2, 4))


def get_color_from_hexa(hexa: str):
    """
    Retourne le nom de la couleur la plus proche dans 'fichier_couleur.txt'.
    :param hexa: Couleur hexadécimale à comparer.
    """
    try:
        # Lecture du fichier fichier_couleur.txt contenant les couples (nom_couleur;code_hex)
        colours = file_management.read_file("fichier_couleur")
    except:
        return None

    target_rgb = hexa_to_rgb(hexa)  # Conversion de la couleur cible en RGB

    min_distance = float('inf')  # Distance minimale initiale infinie
    closest_color = None

    # Parcours de toutes les couleurs du fichier
    for nom_couleur, hexa_ref in colours:
        rgb_ref = hexa_to_rgb(hexa_ref)

        # Calcul de la distance euclidienne simplifiée
        # distance euclidienne simplifiée
        distance = sum((a - b) ** 2 for a, b in zip(target_rgb, rgb_ref))

        # Si une couleur est plus proche, on l’enregistre
        if distance < min_distance:
            min_distance = distance
            closest_color = nom_couleur

    return closest_color


def get_feet_colors_hex(marty: Marty):
    """
    Récupère la couleur détectée par le capteur du pied gauche de Marty en hexadécimal.

    Args:
        marty (Marty): instance du robot.

    Returns:
        str | None: code couleur hexadécimal ou None en cas d'erreur.
    """
    try:
        # Récupère les données brutes (clear, red, green, blue) du capteur gauche
        _, raw_left = marty.client._get_color_sensor_raw_data("left")
        rgb_left = (raw_left[1], raw_left[2], raw_left[3])
        hex_left = rgb_to_hex(rgb_left)
        return hex_left
    except Exception as e:
        print(f"Erreur lors de la lecture des capteurs couleur : {e}")
        return None

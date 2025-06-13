from martypy import Marty
import mmap
import time
import file_management as file_management

def battery(Marty):
    print("Marty's battery level:")
    try:
        battery = float(Marty.get_battery_remaining())
        return battery
    
    except Exception as e:
        print(f"Failed to read Marty batttery lvl: {e}")


def distance(Marty: Marty):
    print("Marty's distance:")
    try:
        distance = float(Marty.get_distance_sensor())
        return distance
    
    except Exception as e:
        print(f"Failed to read Marty distance: {e}")


def obstacle(Marty: Marty):
    try:
        obstaclevalue_right_original = float(Marty.get_obstacle_sensor_reading("right"))
        obstaclevalue_left_original = float(Marty.get_obstacle_sensor_reading("left"))
    
    except Exception as e:
        print(f"Failed to read Marty obstacle: {e}")

    print(f"valeur droit: {obstaclevalue_right_original}")
    print(f"valeur gauche: {obstaclevalue_left_original}")


def calibrate(Marty,couleur:str,nom_fichier:str):
    fichier=open(nom_fichier+'.txt','a')
    fichier.write(f"{couleur};{get_feet_colors_hex(Marty)};\n")
    fichier.close()

def rgb_to_hex(rgb):
    """Convertit un tuple RGB en code hexadécimal."""
    return "{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def get_feet_colors_hex(Marty):
    """
    Récupère les couleurs détectées par les capteurs couleur des pieds gauche et droit de Marty au format hexadécimal,
    sans utiliser get_color_sensor_value_by_channel ni get_color_sensor_hex.
    
        Tuple hex_left
    """
    try:
        # Récupère les données brutes (clear, red, green, blue) pour le pied gauche
        _, raw_left = Marty.client._get_color_sensor_raw_data("left")
        rgb_left = (raw_left[1], raw_left[2], raw_left[3])
        hex_left = rgb_to_hex(rgb_left)
        return hex_left
    except Exception as e:
        print(f"Erreur lors de la lecture des capteurs couleur : {e}")
        return None, None

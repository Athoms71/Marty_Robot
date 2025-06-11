from martypy import Marty
import time


def battery(Marty: Marty):
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
        """obstaclebool_right = bool(Marty.foot_obstacle_sensed("right"))
        obstaclebool_left = bool(Marty.foot_obstacle_sensed("left"))"""
        obstaclevalue_right_original = float(
            Marty.get_obstacle_sensor_reading("right"))
        obstaclevalue_left_original = float(
            Marty.get_obstacle_sensor_reading("left"))
    except Exception as e:
        print(f"Failed to read Marty obstacle: {e}")

    """ print(f"valeur bool droit: {obstaclebool_right}")
        print(f"valeur bool gauche: {obstaclebool_left}")"""
    print(f"valeur droit: {obstaclevalue_right_original}")
    print(f"valeur gauche: {obstaclevalue_left_original}")


def colorsensor(Marty: Marty):
    try:
        calibrate(Marty)
    except Exception as e:
        print(f"Failed to read Marty obstacle: {e}")


def get_color(Marty: Marty):
    """This function reads the color sensor values for both left and right sensors."""
    try:
        valeur_couleur_gauche = int(
            Marty.get_ground_sensor_reading("left"))
        valeur_couleur_droite = int(
            Marty.get_ground_sensor_reading("right"))
        return (valeur_couleur_gauche, valeur_couleur_droite)
    except Exception as e:
        print(f"Failed to read Marty color sensor: {e}")


def calibrate(Marty: Marty):
    liste_couleur = ["bleu", "rouge", "vert", "noir"]
    fichier = open("calibration.txt", "w+")
    for couleur in liste_couleur:
        print(f"je calibre la couleur : {couleur} \nmettez la bonne couleur\n")
        time.sleep(1)
        print("en cours.")
        time.sleep(2)
        print("en cours..")
        time.sleep(3)
        valeur_couleur_gauche = int(
            Marty.get_ground_sensor_reading(str("left")))
        valeur_couleur_droite = int(
            Marty.get_ground_sensor_reading(str("right")))
        print("scannez")
        fichier.write(
            f"{couleur};{valeur_couleur_gauche};{valeur_couleur_droite}\n")

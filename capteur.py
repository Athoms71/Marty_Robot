from martypy import Marty
import time
import file_management as file_management

class Capteur:
    def __init__(self, marty: Marty):
        self.marty = marty

    def get_battery(self):
        try:
            return int(self.marty.get_battery_remaining())
        
        except Exception as e:
            print(f"Failed to read Marty batttery lvl: {e}")


    def get_distance(self):
        print("Marty's distance:")
        try:
            return float(self.marty.get_distance_sensor())
        except Exception as e:
            print(f"Failed to read Marty distance: {e}")


    def obstacle(self):
        try:
            """obstaclebool_right = bool(Marty.foot_obstacle_sensed("right"))
            obstaclebool_left = bool(Marty.foot_obstacle_sensed("left"))"""
            obstaclevalue_right_original = float(
                self.marty.get_obstacle_sensor_reading("right"))
            obstaclevalue_left_original = float(
                self.marty.get_obstacle_sensor_reading("left"))
        except Exception as e:
            print(f"Failed to read Marty obstacle: {e}")

        """ print(f"valeur bool droit: {obstaclebool_right}")
            print(f"valeur bool gauche: {obstaclebool_left}")"""
        print(f"valeur droit: {obstaclevalue_right_original}")
        print(f"valeur gauche: {obstaclevalue_left_original}")


    def colorsensor(self, liste_couleur):
        try:
            Capteur.calibrate(self.marty, liste_couleur)
            content = file_management.read_file("calibration.txt")
            print(content)
        except Exception as e:
            print(f"Failed to read Marty colorsensor: {e}")



    def calibrate(Marty,liste_couleur):
        fichier = open("calibration.txt", "w")
        for couleur in liste_couleur :
            print(f"je calibre la couleur : {couleur} \nmettez la bonne couleur\n")
            time.sleep(1)
            print("en cours.")
            time.sleep(1)
            print("en cours..")
            time.sleep(1)
            valeur_couleur_gauche =int(Marty.get_ground_sensor_reading (str("left")))
            valeur_couleur_droite =int(Marty.get_ground_sensor_reading (str("right")))
            print("scannez")
            fichier.write(f"{couleur};{valeur_couleur_gauche};{valeur_couleur_droite};\n")
            print("c est ecrit")
        fichier.close()

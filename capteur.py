from martypy import Marty
import MartyController


class Capteur:
    def battery(Marty):
        print("Marty's battery level:")
        try:
            battery = float(Marty.get_battery_remaining())
            print(f" batttery lvl:{battery}%")
        
        except Exception as e:
            print(f"Failed to read Marty batttery lvl: {e}")



    def distance(Marty):
        print("Marty's distance:")
        try:
            distance = float(Marty.get_distance_sensor())
        except Exception as e:
            print(f"Failed to read Marty distance: {e}")

        print(distance)


    def obsacle(Marty):
        try:
            """obstaclebool_right = bool(Marty.foot_obstacle_sensed("right"))
            obstaclebool_left = bool(Marty.foot_obstacle_sensed("left"))"""
            obstaclevalue_right_original = float(Marty.get_obstacle_sensor_reading("right"))
            obstaclevalue_left_original = float(Marty.get_obstacle_sensor_reading("left"))
        except Exception as e:
            print(f"Failed to read Marty obstacle: {e}")

        """ print(f"valeur bool droit: {obstaclebool_right}")
        print(f"valeur bool gauche: {obstaclebool_left}")"""
        print(f"valeur droit: {obstaclevalue_right_original}")
        print(f"valeur gauche: {obstaclevalue_left_original}")


    def  colorsensor(Marty):
        try:
            colorsensor_right_original =int(Marty.get_ground_sensor_reading (str("right" )))

            colorsensor_left_original = int(Marty.get_ground_sensor_reading (str("left") ))
        except Exception as e:
            print(f"Failed to read Marty obstacle: {e}")

        print("right: ", colorsensor_right_original)
        print("left: ", colorsensor_left_original)

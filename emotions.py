from martypy import Marty
import Moves as M
import time


def angry(robot: Marty):
    robot.get_ready()
    robot.disco_color("red")
    robot.eyes("angry", 50, True)
    time.sleep(0.8)
    robot.disco_off()
    robot.eyes("normal", 50, True)


def excited(robot: Marty):
    robot.get_ready()
    robot.disco_color("green")
    robot.eyes("excited", 50, True)
    time.sleep(0.8)
    robot.disco_off()
    robot.eyes("normal", 50, True)


def normal(robot: Marty):
    robot.get_ready()
    robot.disco_color("blue")
    robot.eyes("normal", 50, True)
    time.sleep(0.8)
    robot.disco_off()
    robot.eyes("normal", 50, True)


def wide(robot: Marty):
    robot.get_ready()
    robot.disco_color("yellow")
    robot.eyes("wide", 50, True)
    time.sleep(0.8)
    robot.disco_off()
    robot.eyes("normal", 50, True)


def wiggle(robot: Marty):
    robot.get_ready()
    robot.disco_color("purple")
    robot.eyes("wiggle", 50, True)
    time.sleep(0.8)
    robot.disco_off()
    robot.eyes("normal", 50, True)

from martypy import Marty
import Moves as M
import time


def angry(robot: Marty):
    robot.get_ready()
    robot.disco_color("#ff0000")
    robot.eyes("angry", 50, True)
    time.sleep(0.8)
    robot.disco_off()
    robot.eyes("normal", 50, True)


def excited(robot: Marty):
    robot.get_ready()
    robot.disco_color("#fad700")
    robot.eyes("excited", 50, True)
    time.sleep(0.8)
    robot.disco_off()
    robot.eyes("normal", 50, True)


def normal(robot: Marty):
    robot.get_ready()
    robot.disco_color("#0000c0")
    robot.eyes("normal", 50, True)
    time.sleep(0.8)
    robot.disco_off()
    robot.eyes("normal", 50, True)


def wide(robot: Marty):
    robot.get_ready()
    robot.disco_color("#4080ff")
    robot.eyes("wide", 50, True)
    time.sleep(0.8)
    robot.disco_off()
    robot.eyes("normal", 50, True)


def wiggle(robot: Marty):
    robot.get_ready()
    robot.disco_color("#e040e0")
    robot.eyes("wiggle", 50, True)
    time.sleep(0.8)
    robot.disco_off()
    robot.eyes("normal", 50, True)

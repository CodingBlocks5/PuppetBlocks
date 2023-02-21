#
#   @file : PuppetBlock.py
#   @authors : PuppetBlocks team
#   @date : 21 February 2023
#
import time

from machine import Pin, ADC
from servo import Servo

from Screen import Screen
from Audio import Speaker


class Movement:
    __servoPitch = Servo(Pin(26))
    __servoRotation = Servo(Pin(14))
    __joystickPitch = ADC(Pin(39))
    __joystickRotation = ADC(Pin(36))
    __valuePitch = 0
    __valueRotation = 0
    __recording = [(0, 0) for _ in range(50)]
    __isInitialized = False

    @staticmethod
    def __initialize():
        if not Movement.__isInitialized:
            Movement.__joystickPitch.atten(ADC.ATTN_11DB)
            Movement.__joystickRotation.atten(ADC.ATTN_11DB)

    @staticmethod
    def __linespace(start, stop, length):
        start, stop, length = float(start), float(stop), int(length)
        if length == 1:
            yield stop
        else:
            step = (stop - start) / length
            for index in range(length):
                yield start + step * index

    @staticmethod
    def setPitch(value):
        if not Movement.__servoPitch:
            Movement.__initialize()
        angle = int(value)
        Movement.__servoPitch.write_angle(angle)
        Movement.__valuePitch = angle

    @staticmethod
    def setRotation(value):
        if not Movement.__servoRotation:
            Movement.__initialize()
        angle = int(value)
        Movement.__servoRotation.write_angle(angle)
        Movement.__valueRotation = angle

    @staticmethod
    def slidePitch(value, length):
        for val in Movement.__linespace(Movement.__valuePitch, value, length):
            Movement.setPitch(val)
            time.sleep(0.1)
        Movement.setPitch(value)

    @staticmethod
    def slideRotation(value, length):
        for val in Movement.__linespace(Movement.__valueRotation, value, length):
            Movement.setRotation(val)
            time.sleep(0.1)
        Movement.setRotation(value)

    @staticmethod
    def getPitch():
        Movement.__initialize()
        return Movement.__joystickPitch.read() / 4096

    @staticmethod
    def getRotation():
        Movement.__initialize()
        return Movement.__joystickRotation.read() / 4096

    @staticmethod
    def recordJoystick():
        Movement.__initialize()
        Movement.__recording = []
        for _ in range(50):
            Movement.__recording.append((Movement.getPitch(), Movement.getRotation()))
            time.sleep(0.1)

    @staticmethod
    def performRecording():
        for pitch, rotation in Movement.__recording:
            Movement.setPitch(pitch)
            Movement.setRotation(rotation)
            time.sleep(0.1)


class Screens:
    pass

class Audio:
    pass

class Files:
    pass

class Time:
    pass

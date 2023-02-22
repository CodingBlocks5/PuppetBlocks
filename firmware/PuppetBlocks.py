#
#   @file : PuppetBlock.py
#   @authors : PuppetBlocks team
#   @date : 21 February 2023
#
import os
import time
import shutil
import urequests

from machine import Pin, ADC, RTC, SDCard
from framebuf import FrameBuffer, MONO_HLSB

from Servo import Servo
from Screen import Screen
from Audio import Speaker


sd = SDCard(
    slot=2,
    width=1,
    cd=None,
    wp=None,
    sck=Pin(18),
    miso=Pin(19),
    mosi=Pin(23),
    cs=Pin(5),
    freq=20000000
)
os.mount(sd, "/sd")

BASE_DIRECTORY = '/sd/PuppetBlocks/'

class Movement:
    __servoPitch        = Servo(Pin(26))
    __servoRotation     = Servo(Pin(14))
    __joystickPitch     = ADC(Pin(36))
    __joystickRotation  = ADC(Pin(39))
    __valuePitch        = 180
    __valueRotation     = 180
    __recording         = [(0, 0) for _ in range(50)]
    __isInitialized     = False

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
        for val in Movement.__linespace(Movement.__valuePitch, value, length * 10):
            Movement.setPitch(val)
            time.sleep(0.1)
        Movement.setPitch(value)

    @staticmethod
    def slideRotation(value, length):
        for val in Movement.__linespace(Movement.__valueRotation, value, length * 10):
            Movement.setRotation(val)
            time.sleep(0.1)
        Movement.setRotation(value)

    @staticmethod
    def getPitch():
        Movement.__initialize()
        return (1.0 - (Movement.__joystickPitch.read() / 4096)) * 360

    @staticmethod
    def getRotation():
        Movement.__initialize()
        return (1.0 - (Movement.__joystickRotation.read() / 4096)) * 360

    @staticmethod
    def performLive(length):
        for _ in range(length * 10):
            Movement.setPitch(Movement.getPitch())
            Movement.setRotation(Movement.getRotation())
            time.sleep(0.1)

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
    LEFT_SCREEN     = 1
    RIGHT_SCREEN    = 2
    BOTH_SCREENS    = 3
    
    __leftScreen = Screen(addr=0x3c)
    __rightScreen = Screen(addr=0x3d)

    @staticmethod
    def showImage(filename, screen):
        with open(BASE_DIRECTORY + filename, 'rb') as file:
            file.readline()
            file.readline()
            file.readline()
            data = bytearray(file.read())
        file_buffer = FrameBuffer(data, 128, 64, MONO_HLSB)
        if screen == Screens.LEFT_SCREEN or screen == Screens.BOTH_SCREENS:
            Screens.__leftScreen.invert(1)
            Screens.__leftScreen.blit(file_buffer, 0, 0)
            Screens.__leftScreen.show()
        if screen == Screens.RIGHT_SCREEN or screen == Screens.BOTH_SCREENS:
            Screens.__rightScreen.invert(1)
            Screens.__rightScreen.blit(file_buffer, 0, 0)
            Screens.__rightScreen.show()

    @staticmethod
    def showText(text, screen):
        if screen == Screens.LEFT_SCREEN or screen == Screens.BOTH_SCREENS:
            Screens.__leftScreen.fill(0)
            Screens.__leftScreen.text(text, 0, 0, 1)
            Screens.__leftScreen.show()
        if screen == Screens.RIGHT_SCREEN or screen == Screens.BOTH_SCREENS:
            Screens.__rightScreen.fill(0)
            Screens.__rightScreen.text(text, 0, 0, 1)
            Screens.__rightScreen.show()

    @staticmethod
    def blackScreen(screen):
        if screen == Screens.LEFT_SCREEN or screen == Screens.BOTH_SCREENS:
            Screens.__leftScreen.fill(0)
            Screens.__leftScreen.show()
        if screen == Screens.RIGHT_SCREEN or screen == Screens.BOTH_SCREENS:
            Screens.__rightScreen.fill(0)
            Screens.__rightScreen.show()

    @staticmethod
    def whiteScreen(screen):
        if screen == Screens.LEFT_SCREEN or screen == Screens.BOTH_SCREENS:
            Screens.__leftScreen.fill(1)
            Screens.__leftScreen.show()
        if screen == Screens.RIGHT_SCREEN or screen == Screens.BOTH_SCREENS:
            Screens.__rightScreen.fill(1)
            Screens.__rightScreen.show()


class Audio:
    __speaker = Speaker

    @staticmethod
    def synchronousPlay(filename, loop):
        Audio.__speaker.play(BASE_DIRECTORY + filename, loop=loop)
        while Speaker.isplaying() == True:
            pass

    @staticmethod
    def asynchronousPlay(filename, loop):
        Audio.__speaker.play(BASE_DIRECTORY + filename, loop=loop)

    @staticmethod
    def pause():
        Audio.__speaker.pause()

    @staticmethod
    def resume():
        Audio.__speaker.resume()

    @staticmethod
    def stop():
        Audio.__speaker.stop()

    @staticmethod
    def isPlaying():
        return Audio.__speaker.isplaying()


class Files:

    @staticmethod
    def loadFile(filename, url):
        request = urequests.get(url, stream=True)
        if request.status_code == 200:
            with open(BASE_DIRECTORY + filename, 'wb') as file:
                shutil.copyfileobj(request.raw, file)
        print('The file has downloaded!')

    @staticmethod
    def fileExists(filename):
        return filename in Files.listFiles()

    @staticmethod
    def deleteFile(filename):
        os.remove(BASE_DIRECTORY + filename)

    @staticmethod
    def renameFile(filename, newname):
        os.rename(BASE_DIRECTORY + filename, BASE_DIRECTORY + newname)

    @staticmethod
    def listFiles():
        return os.listdir(BASE_DIRECTORY[0:-1])


class Time:
    YEAR        = 1
    MONTH       = 2
    DAY         = 3
    HOUR        = 4
    MINUTE      = 5
    SECOND      = 6

    __RTC       = RTC()

    @staticmethod
    def __timeToInt(time):
        (year, month, day, hour, minute, second) = time
        return  365 * 24 * 60 * 60 * year + \
                30 * 24 * 60 * 60 * month + \
                24 * 60 * 60 * day + \
                60 * 60 * hour + \
                60 * minute + \
                second

    @staticmethod
    def sleep(length, unit):
        if unit == Time.YEAR:
            time.sleep(365 * 24 * 60 * 60 * length)
        elif unit == Time.MONTH:
            time.sleep(30 * 24 * 60 * 60 * length)
        elif unit == Time.DAY:
            time.sleep(24 * 60 * 60 * length)
        elif unit == Time.HOUR:
            time.sleep(60 * 60 * length)
        elif unit == Time.MINUTE:
            time.sleep(60 * length)
        elif unit == Time.SECOND:
            time.sleep(length)

    @staticmethod
    def sleepUntil(final_time):
        current_time = Time.__timeToInt(Time.getTime())
        desired_time = Time.__timeToInt(final_time)
        while current_time < desired_time:
            time.sleep(0.1)
            current_time = Time.__timeToInt(Time.getTime())

    @staticmethod
    def getTime():
        (year, month, day, _, hour, minute, second, _) = Time.__RTC.datetime()
        return (year, month, day, hour, minute, second)

    @staticmethod
    def addTime(source_time, value, unit):
        (year, month, day, hour, minute, second) = source_time
        if unit == Time.YEAR:
            return (year + value, month, day, hour, minute, second)
        elif unit == Time.MONTH:
            return (year, month + value, day, hour, minute, second)
        elif unit == Time.DAY:
            return (year, month, day + value, hour, minute, second)
        elif unit == Time.HOUR:
            return (year, month, day, hour + value, minute, second)
        elif unit == Time.MINUTE:
            return (year, month, day, hour, minute + value, second)
        elif unit == Time.SECOND:
            return (year, month, day, hour, minute, second + value)
        else:
            return (year, month, day, hour, minute, second)

    @staticmethod
    def getTimeUnit(unit):
        (year, month, day, hour, minute, second) = Time.getTime()
        if unit == Time.YEAR:
            return year
        elif unit == Time.MONTH:
            return month
        elif unit == Time.DAY:
            return day
        elif unit == Time.HOUR:
            return hour
        elif unit == Time.MINUTE:
            return minute
        elif unit == Time.SECOND:
            return second
        else:
            return -1

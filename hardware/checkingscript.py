import PuppetBlocks

import time
#Screens -----------------------------------------------------------------------------

#blackScreen, whiteScreen
PuppetBlocks.Screens.blackScreen(3)
time.sleep(1)
PuppetBlocks.Screens.whiteScreen(3)
time.sleep(1)
PuppetBlocks.Screens.blackScreen(1)

#showImage
time.sleep(2)
PuppetBlocks.Screens.showImage('try.pbm', 2)

#showtext
time.sleep(3)
PuppetBlocks.Screens.showText('iot',1)
time.sleep(1)
PuppetBlocks.Screens.showText('fun',2)
time.sleep(1)
PuppetBlocks.Screens.showText('hi',3)

#Audio -------------------------------------------------------------------------------
#synchronousPlay
PuppetBlocks.Audio.synchronousPlay('play.wav',False)
time.sleep(2)

#asynchronousPlay, pause, resume, stop, isPlaying
PuppetBlocks.Audio.asynchronousPlay('sound.wav',False)
print("is playing - ", PuppetBlocks.Audio.isPlaying())
time.sleep(5)
PuppetBlocks.Audio.pause()
time.sleep(3)
PuppetBlocks.Audio.resume()
time.sleep(5)
PuppetBlocks.Audio.stop()
print("is playing - ", PuppetBlocks.Audio.isPlaying())

#Files -------------------------------------------------------------------------------
#fileExists
print("exist - ",PuppetBlocks.Files.fileExists('check.pbm')) #prints False
time.sleep(2)

#loadFile
PuppetBlocks.Files.loadFile('check.pbm', 'https://firebasestorage.googleapis.com/v0/b/puppetblocks.appspot.com/o/scatman.3.pbm?alt=media&token=ae2dcc4d-12d4-405b-8d0b-65eb7d3a8504')
print("exist - ", PuppetBlocks.Files.fileExists('check.pbm')) #should print True
time.sleep(1)

#deleteFile
PuppetBlocks.Files.deleteFile('check.pbm')
time.sleep(1)
print("exist - ",PuppetBlocks.Files.fileExists('check.pbm')) #should print False

#renameFile, listFiles
print(PuppetBlocks.Files.listFiles())
time.sleep(2)
PuppetBlocks.Files.renameFile('try.pbm','try1.pbm')
print(PuppetBlocks.Files.listFiles())
time.sleep(5)

#Time --------------------------------------------------------------------------------------------
#getTime
print(PuppetBlocks.Time.getTime())
a = PuppetBlocks.Time.getTime()

#sleep
PuppetBlocks.Time.sleep(2, PuppetBlocks.Time.SECOND)
print(a) #should be after 2 seconds

#addTime, sleepUntil
b = PuppetBlocks.Time.addTime(a, 1, PuppetBlocks.Time.MINUTE)
print(b)
PuppetBlocks.Time.sleepUntil(b)

#Movement ----------------------------------------------------------------------------------------
#setPitch, setRotaion, getRotation, getPitch
PuppetBlocks.Movement.setPitch(0) #down
print(PuppetBlocks.Movement.getPitch())
time.sleep(2)
PuppetBlocks.Movement.setRotation(0) #left
time.sleep(2)
PuppetBlocks.Movement.setRotation(180) #right
print(PuppetBlocks.Movement.getRotation())

#slidePitch, slideRotation
time.sleep(1)
PuppetBlocks.Movement.slidePitch(0, 5) #down
print(PuppetBlocks.Movement.getPitch())
time.sleep(2)
PuppetBlocks.Movement.slideRotation(0, 5) #left
print(PuppetBlocks.Movement.getRotation())
time.sleep(2)

#recordJoystick, performRecording
PuppetBlocks.Movement.recordJoystick()
print("joystick movement - " ,PuppetBlocks.Movement.__recording)
time.sleep(1)
PuppetBlocks.Movement.performRecording()
time.sleep(1)

#preformLive
PuppetBlocks.Movement.performLive(5)
PuppetBlocks.Files.renameFile('try1.pbm','try.pbm')
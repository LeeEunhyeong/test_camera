import picamera
from time import sleep

camera = picamera.PiCamera()
camera.capture('image.jpg')

camera.start_preview()
camera.vflip = True
camera.hflip = True
camera.brightness = 60

camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()
#-완전 기본 파메라.....
#-----------
for i in range(100):
    camera.brightness = i
    sleep(0.1)

#master branch don't have this point

#----hand conflict ----------

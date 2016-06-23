from picamera.array import PiRGBArray
from picamera import piCamera
import time
import cv2

camera = piCamera()
camera.resolution = (480,320)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size = (480,320))

tiem.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format = 'bgr', use_video_=True):
	image = frame.array
	cv2.imshow('Frame',image)
	key = cv2.waitKey(1) & 0xff
	if key ==27:
		break
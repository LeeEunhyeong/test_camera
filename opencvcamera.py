import subprocess
from SimpleCV import Image
import time
#using opencv captured image, but purpose is make by video
call(“raspistill -n -t 0 -w %s -h %s -o image.bmp” % 640 480, shell=True)

img = Image(“image.bmp”)

img.show()
time.sleep(5)

#--------
cam = Camera()
img = cam.getImage()

#-----
img = img.edges()
img.show()
time.sleep(5)


img = img.binarize()
img.show()
time.sleep(5) 


img = img.findBlobs()
for blob in blobs:
    blob.draw()  
img.show()
time.sleep(5) 
#연속적인 이미지 촬영으로 영상을 만들면 속도가 너무 느리다 한방으로 가자
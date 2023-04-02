import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

name = 'Aum'  # replace with different name to train for a different person.

#use variable camera as the picamera
camera = PiCamera()
#previews camera
camera.start_preview()
#takes 10 pictures, waiting 4 secs between each take.
for i in range(10):
    sleep(4)
    camera.capture('/dataset/{}/image{}.jpg'.format(name, i))
camera.stop_preview()
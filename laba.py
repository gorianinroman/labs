#from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
camera.contrast=80
camera.brightness=80
camera.start_preview()
time.sleep(5)

camera.stop_preview()
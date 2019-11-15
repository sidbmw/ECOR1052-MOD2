from picamera import PiCamera
camera = PiCamera()
camera.resolution = (800, 480)
camera.vflip = True
camera.start_preview(alpha = 128)

#import time
from time import gmtime, strftime
output = strftime("/home/pi/Desktop/L8-6/image-%d-%m %H: %M.png", gmtime())

def take_picture():
    camera.capture(output)
    camera.stop_preview()
    
    
take_picture()
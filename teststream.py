from imutils.video import VideoStream
from time import sleep
import cv2

vs = VideoStream(usePiCamera = True).start()
sleep(2.0)

while True:
    frame = vs.read()
    frame = cv2.flip(frame, 0)
    
    cv2.imshow("Video stream", frame)
    cv2.waitKey(1)
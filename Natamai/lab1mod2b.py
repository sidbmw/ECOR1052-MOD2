import RPi.GPIO as GPIO #Library for the GPIO Pins
import time #Library for time-related tasks

lst = [25, 8, 7, 1, 12, 16, 20, 21]
lst2 = [25, 7, 12, 20, 8, 1, 16, 21]
GPIO.setmode(GPIO.BCM) #Sets the way we reference the GPIO Pins
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)




#turn all ligths off


for i in range(250):
    GPIO.output(25, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(1, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    
    print(i)
    if i % 2 == 1:
        GPIO.output(21, GPIO.HIGH)
    i = i // 2
    
    #time.sleep(.1)
   # GPIO.output(21, GPIO.LOW)

    if i % 2 == 1:
        GPIO.output(20, GPIO.HIGH)
    i = i // 2
        
   # time.sleep(.1)
    #GPIO.output(20, GPIO.LOW)
    
    if i % 2 == 1:
        GPIO.output(16, GPIO.HIGH)
    i = i // 2
        
    #time.sleep(.1)
#    GPIO.output(16, GPIO.LOW)

    if i % 2 == 1:
        GPIO.output(12, GPIO.HIGH)
    i = i // 2
        
    #time.sleep(.1)
#    GPIO.output(12, GPIO.LOW)

    if i % 2 == 1:
        GPIO.output(1, GPIO.HIGH)
    i = i // 2
        
    #time.sleep(.1)
#    GPIO.output(1, GPIO.LOW)

    if i % 2 == 1:
        GPIO.output(7, GPIO.HIGH)
    i = i // 2
        
    #time.sleep(.1)
    #GPIO.output(7, GPIO.LOW)

    if i % 2 == 1:
        GPIO.output(8, GPIO.HIGH)
    i = i // 2
        
    #time.sleep(.1)
    #GPIO.output(8, GPIO.LOW)

    if i % 2 == 1:
        GPIO.output(25, GPIO.HIGH)
    i = i // 2
        
    time.sleep(1)
    #GPIO.output(25, GPIO.LOW)
    





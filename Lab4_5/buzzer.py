import time
import RPi.GPIO as GPIO

print("Setup") #informs user setup has begun

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT) #sets GPIO pin 25 as an output

GPIO.setup(24, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)


pin = GPIO.PWM(25,1000) #set pin 25 as a PWM output, with a frequency of 50 Hz
#pin.start(0) #sets the starting duty cycle of the PWM signal to 0%
time.sleep(1)

print("Begin") #informs user the main function of the program is beginning

i = 0
for i in range(5):
    print(i)
    pin.start(0)
    pin.ChangeDutyCycle(50) #change the duty cycle to 50%
    time.sleep(1)
    pin.stop()
    time.sleep(1)
    
    if i == 5:
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
    if i == 4:
        GPIO.output(12, GPIO.LOW)
    if i == 3:
        GPIO.output(1, GPIO.LOW)
    if i == 2:
        GPIO.output(7, GPIO.LOW)
    if i == 1:
        GPIO.output(8, GPIO.LOW)
    if i == 0:
        GPIO.output(24, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)    
        time.sleep(3)
        
    i-=1

GPIO.cleanup()

print("Done")

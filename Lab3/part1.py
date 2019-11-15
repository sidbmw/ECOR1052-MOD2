#
#import RPi.GPIO as GPIO
#import time
#
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(20, GPIO.OUT)
#GPIO.setup(21, GPIO.OUT)
#
#
#GPIO.output(20, GPIO.HIGH) #CW
#time.sleep(1)
#
#
#
#GPIO.output(20, GPIO.LOW)
#time.sleep(1)
#
#
#
#
#GPIO.output(21, GPIO.HIGH) #CCW
#time.sleep(1)
#
#GPIO.output(21, GPIO.LOW)
#time.sleep(1)
#
#GPIO.cleanup()
#


import RPi.GPIO as GPIO
import time

#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=15
GPIO.setup(buzzer,GPIO.OUT)
#Run forever loop
while True:
    GPIO.output(buzzer,GPIO.HIGH)
    #print ("Beep")
    #sleep(0.00005) # Delay in seconds
    time.sleep(1/1000000.0)
    GPIO.output(buzzer,GPIO.LOW)
    #print ("No Beep")
    time.sleep(1/1000000.0)
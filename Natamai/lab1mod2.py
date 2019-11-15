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
#Sets GPIO Pin 25 to an output pin
i = 0
for x in range(len(lst)): #iterates through      the loop 5 times

    print ("LED on") #Prints when the LED turns on in the console below
    GPIO.output(lst[i],GPIO.HIGH) #Sets the voltage of Pin 25 'HIGH' or 3.3V
    time.sleep(0.4) #Pauses the program for 1 second
    i += 1
i = 0
for x in range(len(lst2)): #iterates through      the loop 5 times
    print ("LED off") #Prints when the LED turns off in the console below
    GPIO.output(lst2[i ],GPIO.LOW) #Sets the voltage of Pin 25 'LOW' or 0V
    time.sleep(0.4) #Pauses the program for 1 second
    i += 1
GPIO.cleanup()#Resets the GPIO Pins that we used
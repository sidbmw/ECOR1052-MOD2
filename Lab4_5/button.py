import RPi.GPIO as GPIO
import time
#import lcd_i2c
GPIO.setmode(GPIO.BCM)

GPIO.setup(9,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pulls the voltage of the pin to 0V when nothing is connected


#Setup and initialization functions of the LCD
#def printLCD(string1, string2):
#    lcd_i2c.printer(string1, string2)

#def setup():
#    lcd_i2c.lcd_init()

try:
#    setup() #calls setup function
    while True:
#        printLCD("Press the button!!"," ") #prints to LCD
        if(GPIO.input(9) == GPIO.HIGH): #Checks if input is high (3.3V) if so the button is pressed (connects 3.3V rail to pin)
            print("Button Pressed!!!")
            time.sleep(2)
        time.sleep(0.1)


except KeyboardInterrupt:
    pass

GPIO.cleanup()
lcd_i2c.cleanup()
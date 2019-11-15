import RPi.GPIO as GPIO
import time

#GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#BUZZER

pwm_buzzer = GPIO.PWM(15, 1000)
#pwm_buzzer.start(50)
#time.sleep(1)
#pwm_buzzer.start(0)

pwm = GPIO.PWM(19, 50) 
pwm2 = GPIO.PWM(26, 50)

try:
    print("In TRY")
    while (1):
#        printLCD("Press the button!!"," ") #prints to LCD
        time.sleep(2)
        if(GPIO.input(23) == GPIO.HIGH): #Checks if input is high (3.3V) if so the button is pressed (connects 3.3V rail to pin)
            print("Button Pressed!!!")
            GPIO.output(5, GPIO.HIGH)
            pwm_buzzer.start(50)
            time.sleep(1)
            pwm_buzzer.stop()
            for i in range(50):
                pwm.start(0)
                pwm.ChangeDutyCycle(i)
                time.sleep(0.1)
                #GPIO.output(19, GPIO.HIGH)          
                print(i)
                pwm.stop()
            pwm.ChangeDutyCycle(0)
#            GPIO.output(19, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            
        if(GPIO.input(22) == GPIO.HIGH): #Checks if input is high (3.3V) if so the button is pressed (connects 3.3V rail to pin)
            print("Button Pressed!!!")
            GPIO.output(5, GPIO.HIGH)
            pwm_buzzer.start(50)
            time.sleep(1)
            pwm_buzzer.stop()
            for i in range(50):
                pwm.start(0)
                pwm.ChangeDutyCycle(i)
                time.sleep(0.1)
                #GPIO.output(19, GPIO.HIGH)          
                print(i)
                pwm.stop()
            pwm.ChangeDutyCycle(0)
#            GPIO.output(19, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
#j = 0
#pwm2 = GPIO.PWM(21, 50)
#print("starting)")
#for i in range(50):
#    pwm2.start(j)
#    time.sleep(0.1)
#    j += 1
#    print(j)
        

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()

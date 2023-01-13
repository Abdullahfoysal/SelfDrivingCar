import RPi.GPIO as GPIO
from time import sleep

motor1A = 8
motor1B =10
motor1E=12

motor2E=33
motor2A = 35
motor2B =37


GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1A,GPIO.OUT)
GPIO.setup(motor1B,GPIO.OUT)
GPIO.setup(motor1E,GPIO.OUT)
GPIO.setup(motor2A,GPIO.OUT)
GPIO.setup(motor2B,GPIO.OUT)
GPIO.setup(motor2E,GPIO.OUT)

p1 = GPIO.PWM(motor1E,100)
p2 = GPIO.PWM(motor2E,100)




def motor(a,b):
    if (a>=0 and b>=0):
        GPIO.output(motor1A,False)
        GPIO.output(motor1B,True)
        
        GPIO.output(motor2A,False)
        GPIO.output(motor2B,True)

    else:
        
        GPIO.output(motor1A,True)
        GPIO.output(motor1B,False) 
        
        GPIO.output(motor2A,True)
        GPIO.output(motor2B,False)
        
    p1.start(abs(a))
    p2.start(abs(b))
   

   

try:
    while True:
        print("Working")
        motor(100,100)
        sleep(3)
        motor(-100,-100)
        sleep(3)
        #motor2Run()
        
except KeyboardInterrupt:
    print("Keyboard Interrupt occured")
except:
    print("Other exception occured")
finally:
    GPIO.cleanup()
    print("clean exit")
               
import RPi.GPIO as GPIO
from time import sleep
motor1A = 8
motor1B =10
motor1E=12
motor2A = 7
motor2B =5
motor2E=3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1A,GPIO.OUT)
GPIO.setup(motor1B,GPIO.OUT)
GPIO.setup(motor1E,GPIO.OUT)
GPIO.setup(motor2A,GPIO.OUT)
GPIO.setup(motor2B,GPIO.OUT)
GPIO.setup(motor2E,GPIO.OUT)

p = GPIO.PWM(motor1E,100)
q = GPIO.PWM(motor2E,100)

def motor(a,b):
    if (a>=0):
        GPIO.output(motor1A,True)
        GPIO.output(motor1B,False)

    else:
        GPIO.output(motor1A,False)
        GPIO.output(motor1B,True)

    if (b>=0):
        GPIO.output(motor2A,True)
        GPIO.output(motor2B,False)

    else:
        GPIO.output(motor2A,False)
        GPIO.output(motor2B,True)
    p.start(abs(a))
    q.start(abs(b))

while True:
    motor(100,100)
    sleep(5)
    motor(-100,-100)
    sleep(5)
    motor(10,10)
    sleep(5)


GPIO.cleanup()

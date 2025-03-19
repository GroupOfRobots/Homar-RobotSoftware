import RPi.GPIO as GPIO

SERVO_PIN = 19

class ServoMotor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SERVO_PIN, GPIO.OUT)
        self.servo = GPIO.PWM(SERVO_PIN, 50)
        self.down_pos = 12.8
        self.up_pos = 9.5
        self.servo.start(0)

    def moveUp(self):
        self.servo.ChangeDutyCycle(self.up_pos)
  
    def moveDown(self):
        self.servo.ChangeDutyCycle(self.down_pos)
  

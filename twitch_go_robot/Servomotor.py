import RPi.GPIO as GPIO
import time


class ServoMotor:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.servo = GPIO.PWM(pin, 50)
        self.pin = pin
        self.down_pos = 12.8
        self.up_pos = 9.5
        self.servo.start(0)
        time.sleep(1)

    def moveUp(self):
        self.servo.ChangeDutyCycle(self.up_pos)
        time.sleep(1)

    def moveDown(self):
        self.servo.ChangeDutyCycle(self.down_pos)
        time.sleep(1)

    def delete(self):
        self.servo.stop()
        # GPIO.cleanup()


def main():
    print("Hello World from servomotr!")
    servo = ServoMotor(19)
    servo.moveUp()
    servo.moveDown()
    servo.delete()


if __name__ == "__main__":
    main()

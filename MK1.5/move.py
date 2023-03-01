import RPi.GPIO as GPIO
import time


# define pins
standby_pin = 25

pwm_b_pin = 18
b_in_1_pin = 24
b_in_2_pin = 23

pwm_a_pin = 13
a_in_1_pin = 16
a_in_2_pin = 20


class Movement:

    def __init__(self):
        self.standby_pin = standby_pin

        self.pwm_b_pin = pwm_b_pin
        self.b_in_1_pin = b_in_1_pin
        self.b_in_2_pin = b_in_2_pin

        self.pwm_a_pin = pwm_a_pin
        self.a_in_1_pin = a_in_1_pin
        self.a_in_2_pin = a_in_2_pin


    def setup(self):
        # turn off warnings
        GPIO.setwarnings(False)
        # set mode of numbering pins
        GPIO.setmode(GPIO.BCM)

        # set pins mode
        # motors driver
        GPIO.setup(self.standby_pin, GPIO.OUT)
        GPIO.output(self.standby_pin, GPIO.HIGH)

        # motor B
        GPIO.setup(self.pwm_b_pin, GPIO.OUT)
        self.pwm_b_pin = GPIO.PWM(self.pwm_b_pin, 1000)
        GPIO.setup(self.b_in_1_pin, GPIO.OUT)
        GPIO.setup(self.b_in_2_pin, GPIO.OUT)

        # motor A
        GPIO.setup(self.pwm_a_pin, GPIO.OUT)
        self.pwm_a_pin = GPIO.PWM(self.pwm_a_pin, 1000)
        GPIO.setup(self.a_in_1_pin, GPIO.OUT)
        GPIO.setup(self.a_in_2_pin, GPIO.OUT)
        # self.pwm_b_pin.ChangeDutyCycle(75) # change PWM value


    def move_foward(self, pwm_value, work_time=None):
        GPIO.output(self.b_in_1_pin, GPIO.LOW)
        GPIO.output(self.b_in_2_pin, GPIO.HIGH)
        self.pwm_b_pin.start(pwm_value)

        GPIO.output(self.a_in_1_pin, GPIO.LOW)
        GPIO.output(self.a_in_2_pin, GPIO.HIGH)
        self.pwm_a_pin.start(pwm_value)

        if work_time:
            time.sleep(work_time)


    def move_backward(self, pwm_value, work_time=None):
        GPIO.output(self.b_in_1_pin, GPIO.HIGH)
        GPIO.output(self.b_in_2_pin, GPIO.LOW)
        self.pwm_b_pin.start(pwm_value)

        GPIO.output(self.a_in_1_pin, GPIO.HIGH)
        GPIO.output(self.a_in_2_pin, GPIO.LOW)
        self.pwm_a_pin.start(pwm_value)

        if work_time:
            time.sleep(work_time)

    def turn_right(self, pwm_value, work_time=None):
        GPIO.output(self.b_in_1_pin, GPIO.HIGH)
        GPIO.output(self.b_in_2_pin, GPIO.LOW)
        self.pwm_b_pin.start(pwm_value)

        GPIO.output(self.a_in_1_pin, GPIO.LOW)
        GPIO.output(self.a_in_2_pin, GPIO.HIGH)
        self.pwm_a_pin.start(pwm_value)

        if work_time:
            time.sleep(work_time)


    def turn_left(self, pwm_value, work_time=None):
        GPIO.output(self.b_in_1_pin, GPIO.LOW)
        GPIO.output(self.b_in_2_pin, GPIO.HIGH)
        self.pwm_b_pin.start(pwm_value)

        GPIO.output(self.a_in_1_pin, GPIO.HIGH)
        GPIO.output(self.a_in_2_pin, GPIO.LOW)
        self.pwm_a_pin.start(pwm_value)

        if work_time:
            time.sleep(work_time)

    def stop(self):
        GPIO.output(self.b_in_1_pin, GPIO.HIGH)
        GPIO.output(self.b_in_2_pin, GPIO.HIGH)
        self.pwm_b_pin.start(0)

        GPIO.output(self.a_in_1_pin, GPIO.HIGH)
        GPIO.output(self.a_in_2_pin, GPIO.HIGH)
        self.pwm_a_pin.start(0)

# movement = Movement()
# movement.setup()
# movement.move_foward(5, 30)
# movement.move_backward(5, 30)
# movement.turn_right(5, 30)
# movement.turn_left(5, 30)
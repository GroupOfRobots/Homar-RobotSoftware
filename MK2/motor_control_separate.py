import RPi.GPIO as GPIO
import time
from Motor import Motor


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
        self.setup()
        self._r_motor = Motor(pwm_b_pin, b_in_1_pin, b_in_2_pin)
        self._l_motor = Motor(pwm_a_pin, a_in_1_pin, a_in_2_pin)

    def setup(self):
        # turn off warnings
        GPIO.setwarnings(False)
        # set mode of numbering pins
        GPIO.setmode(GPIO.BCM)

        # set pins mode
        # motors driver
        GPIO.setup(self.standby_pin, GPIO.OUT)
        GPIO.output(self.standby_pin, GPIO.HIGH)

    def move_motor_R(self, pwm_valuel, work_time=None):
        self._r_motor.start_motor(pwm_valuel)

        if work_time:
            time.sleep(work_time)

    def move_motor_L(self, pwm_value, work_time=None):
        self._l_motor.start_motor(pwm_value)

        if work_time:
            time.sleep(work_time)

    def stop(self):
        self._r_motor.stop_motor()
        self._l_motor.stop_motor()


# movement = Movement()
# movement.setup()
# movement.move_motor_R(50, 30)
# movement.move_motor_L(50, 10)

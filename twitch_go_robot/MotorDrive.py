from Motor import Motor
import RPi.GPIO as GPIO
from typing import List

standby_pin = 25

pwm_b_pin = 18
b_in_1_pin = 24
b_in_2_pin = 23

pwm_a_pin = 13
a_in_1_pin = 16
a_in_2_pin = 20


class MotorDrive:
    def __init__(self) -> None:
        self.left_motor = Motor(pwm_a_pin, a_in_1_pin, a_in_2_pin)
        self.right_motor = Motor(pwm_b_pin, b_in_1_pin, b_in_2_pin)

        self._motors_standby_pin = standby_pin
        GPIO.setup(self._motors_standby_pin, GPIO.OUT)
        GPIO.output(self._motors_standby_pin, GPIO.HIGH)

    def move_motors(self, pwms: List[float]) -> None:
        self.left_motor.start_motor(pwms[0])
        self.right_motor.start_motor(pwms[1])

    def stop_motors(self) -> None:
        self.left_motor.stop_motor()
        self.right_motor.stop_motor()

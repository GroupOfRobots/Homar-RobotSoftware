from Motor import Motor

standby_pin = 25

pwm_b_pin = 18
b_in_1_pin = 24
b_in_2_pin = 23

pwm_a_pin = 13
a_in_1_pin = 16
a_in_2_pin = 20


class Robot:
    def __init__(self) -> None:
        self._motors = {"left": Motor(pwm_a_pin, a_in_1_pin, a_in_2_pin), "right": Motor(pwm_b_pin, b_in_1_pin, b_in_2_pin)}
        self._motors_standby_pin = standby_pin

    def start_motor(self, motor_name: str, pwm: int):
        self._motors[motor_name].start_motor(pwm)

    def stop_motor(self, motor_name: str):
        self._motors[motor_name].stop_motor()
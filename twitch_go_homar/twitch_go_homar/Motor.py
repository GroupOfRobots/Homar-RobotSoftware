import RPi.GPIO as GPIO


class Motor:
    def __init__(self, pwm_pin: int, first_in_pin: int, second_in_pin: int) -> None:
        self._first_in_pin = first_in_pin
        self._second_in_pin = second_in_pin

        GPIO.setup(pwm_pin, GPIO.OUT)
        self._pwm_pin = GPIO.PWM(pwm_pin, 1000)
        GPIO.setup(self._first_in_pin, GPIO.OUT)
        GPIO.setup(self._second_in_pin, GPIO.OUT)

    def run(self, pwm_value):
        if pwm_value < 0:
            GPIO.output(self._first_in_pin, GPIO.LOW)
            GPIO.output(self._second_in_pin, GPIO.HIGH)
        elif pwm_value > 0:
            GPIO.output(self._first_in_pin, GPIO.HIGH)
            GPIO.output(self._second_in_pin, GPIO.LOW)
        else:
            GPIO.output(self._first_in_pin, GPIO.HIGH)
            GPIO.output(self._second_in_pin, GPIO.HIGH)
        
        self._pwm_pin.start(abs(pwm_value))

    def stop_motor(self):
        GPIO.output(self._first_in_pin, GPIO.HIGH)
        GPIO.output(self._second_in_pin, GPIO.HIGH)
        self._pwm_pin.start(0)

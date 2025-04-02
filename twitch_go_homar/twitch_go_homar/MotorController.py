import RPi.GPIO as GPIO
from twitch_go_homar.Motor import Motor 
from rclpy.node import Node
from geometry_msgs.msg import Twist
import rclpy

STANDBY_PIN = 25

PWM_A_PIN = 13
A_IN_1_PIN = 16
A_IN_2_PIN = 20

PWM_B_PIN = 18
B_IN_1_PIN = 24
B_IN_2_PIN = 23

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.subscription = self.create_subscription(MotorData, 'cmd_vel', self.listener_callback, 10)
 
        self.left_motor = Motor(PWM_A_PIN, A_IN_1_PIN, A_IN_2_PIN)
        self.right_motor = Motor(PWM_B_PIN, B_IN_1_PIN, B_IN_2_PIN)
        
        self._motors_standby_pin = STANDBY_PIN
        GPIO.setup(self._motors_standby_pin, GPIO.OUT)
        GPIO.output(self._motors_standby_pin, GPIO.HIGH)

    def listener_callback(self, twist):
        pwm_left = twist.y - twist.x
        pwm_right = twist.y + twist.x
        self.move_motors(pwm_left * 1000, pwm_right * 1000)


    def move_motors(self, pwm_left, pwm_right):
        self.left_motor.run(pwm_left)
        self.right_motor.run(pwm_right)


def main(args=None):
    rclpy.init(args=args)
    controller = MotorController()
    rclpy.spin(controller)
    
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

class MotorData:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
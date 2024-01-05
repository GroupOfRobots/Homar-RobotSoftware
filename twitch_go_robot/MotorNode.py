import rclpy
from rclpy.node import Node

from twitch_go_robot.MotorDrive import MotorDrive
from geometry_msgs.msg import Twist

from typing import List

PWM = 100


class MotorNode(Node, MotorDrive):
    def __init__(self):
        super().__init__("MotorNode")
        self.subscription = self.create_subscription(
            Twist, "/cmd_vel", self.move_motor_calbck, 10
        )
        self.subscription  # prevent unused variable warning

    def move_motor_calbck(self, msg: Twist):
        pwms = self.convert_input_to_pwm(msg)
        self.stop_motors(pwms)

    def convert_input_to_pwm(self, input: Twist) -> List[float]:
        # print('input.linear {0} moved to {1} {2}'.format(input.linear.name, input.linear.x, input.linear.y))
        pwm_l = -input.linear.y * PWM / 2 + input.linear.x * PWM / 2
        pwm_r = -input.linear.y * PWM / 2 - input.linear.x * PWM / 2

        return [pwm_l, pwm_r]


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MotorNode()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

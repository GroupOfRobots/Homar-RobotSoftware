import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from typing import List


class Motor:
    def __init__(self, pins: List[int]) -> None:
        pass

    def move(self, pwm: int):
        print(f"MOTOR VALUE: {pwm}")


class MovementController(Node):

    def __init__(self):
        super().__init__('movement_controller')
        self.subscription = self.create_subscription(
             Twist, "/cmd_vel", self.listener_callback, 10)
        self._left_motor = Motor([])
        self._right_motor = Motor([])

    def listener_callback(self, msg: Twist):
        left_right_wheel_ratio = 1-abs(msg.angular.z/3.14)
        faster_wheel = msg.linear.y * 100
        slower_wheel = faster_wheel * left_right_wheel_ratio
        if msg.angular.z >= 0:
            self._left_motor.move(faster_wheel)
            self._right_motor.move(slower_wheel)
        else:
            self._right_motor.move(faster_wheel)
            self._left_motor.move(slower_wheel)


def main(args=None):
    rclpy.init(args=args)

    movement_controller = MovementController()

    rclpy.spin(movement_controller)

    movement_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

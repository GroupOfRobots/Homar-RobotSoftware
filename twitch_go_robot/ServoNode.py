import rclpy
from rclpy.node import Node

from Servomotor import ServoMotor
from geometry_msgs.msg import Twist

PWM = 100


class ServoNode(Node, ServoMotor):
    def __init__(self):
        super().__init__("ServoNode")
        self.subscription = self.create_subscription(
            Twist, "/cmd_vel", self.move_servo_calbck, 10
        )
        self.pin = 123  # TODO
        self.subscription  # prevent unused variable warning

    def move_servo_calbck(self, msg: Twist):
        pass


def main(args=None):
    # rclpy.init(args=args)

    # minimal_subscriber = MotorNode()

    # rclpy.spin(minimal_subscriber)

    # # Destroy the node explicitly
    # # (optional - otherwise it will be done automatically
    # # when the garbage collector destroys the node object)
    # minimal_subscriber.destroy_node()
    # rclpy.shutdown()
    pass


if __name__ == "__main__":
    main()

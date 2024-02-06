import rclpy
from rclpy.node import Node

from Servomotor import ServoMotor
from geometry_msgs.msg import Bool

PWM = 100


class ServoNode(Node):
    def __init__(self):
        self._servo = ServoMotor(19)
        super().__init__("ServoNode")
        self.subscription = self.create_subscription(
            Bool, "/open_servo", self.move_servo_calbck, 10
        )
        self.subscription  # prevent unused variable warning

    def move_servo_calbck(self, msg: Bool):
        if msg.value:
            self._servo.moveUp()
        else:
            self._servo.moveDown()


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = ServoNode()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

    pass


if __name__ == "__main__":
    main()

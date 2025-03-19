from std_msgs.msg import String
import rclpy
from rclpy.node import Node
from twitch_go_homar import ServoMotor


class ServoController(Node):
    def __init__(self):
        super().__init__('servo_controller')
        self.subscription = self.create_subscription(String, 'servo_cmd', self.listener_callback, 10)
        self.servo = ServoMotor()

    def listener_callback(self, msg):
        if msg.data == 'up':
            self.servo.moveUp()
        elif msg.data == 'down':
            self.servo.moveDown()

def main(args=None):
    rclpy.init(args=args)
    controller = ServoController()
    
    rclpy.spin(controller)

    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
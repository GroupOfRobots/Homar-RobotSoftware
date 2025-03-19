import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class XboxController(Node):
    def __init__(self):
        super().__init__('xbox_controller')
        self.subscription = self.create_subscription(Joy, 'joy', self.joy_callback, 10)
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.servo_pub = self.create_publisher(String, 'servo_cmd', 10)
        
    def joy_callback(self, msg):
        twist = Twist()

        # Tutaj tabela zawierajca indeksy przycisków i osi
        # https://index.ros.org/p/joy/
        twist.linear.x = msg.axes[1]  # Przód/tył
        twist.angular.z = msg.axes[0]  # Obrót
        
        self.cmd_vel_pub.publish(twist)
        
        # Przycisk A (msg.buttons[0]) podnosi serwo, Y (msg.buttons[3]) opuszcza
        servo_cmd = String()
        if msg.bkuttons[0]:
            servo_cmd.data = 'up'
        elif msg.buttons[3]:
            servo_cmd.data = 'down'
        
        if servo_cmd.data:
            self.servo_pub.publish(servo_cmd)


def main(args=None):
    rclpy.init(args=args)
    controller = XboxController()

    try:
        rclpy.spin(controller)
    except KeyboardInterrupt:
        pass

    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

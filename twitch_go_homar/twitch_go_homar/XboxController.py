import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from xbox360controller import Xbox360Controller

class XboxController(Node):
    def __init__(self):
        super().__init__('xbox_controller')
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.servo_pub = self.create_publisher(String, 'servo_cmd', 10)
        try:
            with Xbox360Controller(0, axis_threshold=0.2) as controller:
                controller.button_a.when_pressed = self.on_button_a_pressed
                controller.button_y.when_pressed = self.on_button_y_pressed
                controller.axis_l.when_moved = self.on_left_stick_moved
        except Exception as e:
            print('Exception while init controller: ', e)
        
    def on_button_a_pressed(self):
        servo_cmd = String()
        servo_cmd.data = 'up'
        self.servo_pub.publish(servo_cmd)

    def on_button_y_pressed(self):
        servo_cmd = String()
        servo_cmd.data = 'down'
        self.servo_pub.publish(servo_cmd)

    def on_left_stick_moved(self, axis):
        twist = Twist()
        twist.linear.x = axis.x
        twist.angular.z = axis.y
        self.cmd_vel_pub.publish(twist)

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

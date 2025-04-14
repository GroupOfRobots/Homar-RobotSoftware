import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from std_msgs.msg import String
from xbox360controller import Xbox360Controller

class XboxController(Node):
    def __init__(self, reverse_axis_mode=True):
        super().__init__('xbox_controller')
        self.cmd_vel_pub = self.create_publisher(Vector3, 'cmd_vel', 10)
        self.servo_pub = self.create_publisher(String, 'servo_cmd', 10)
        self.reverse_axis_mode = reverse_axis_mode
        try:
            self.controller = Xbox360Controller(0, axis_threshold=0.0)
            self.controller.button_a.when_pressed = self.on_button_a_pressed
            self.controller.button_y.when_pressed = self.on_button_y_pressed
            self.controller.axis_l.when_moved = self.on_left_stick_moved
        except Exception as e:
            self.get_logger().error(f'Exception while init controller: {e}')
        
    def on_button_a_pressed(self):
        servo_cmd = String()
        servo_cmd.data = 'up'
        self.servo_pub.publish(servo_cmd)

    def on_button_y_pressed(self):
        servo_cmd = String()
        servo_cmd.data = 'down'
        self.servo_pub.publish(servo_cmd)

    def on_left_stick_moved(self, axis):
        msg = Vector3(axis.x, -axis.y if self.reverse_axis_mode else axis.y)
        if abs(axis.x) < 0.1:
            msg.x = 0.0
        else:
            msg.x = axis.x

        if abs(axis.y) < 0.1:
            msg.y = 0.0
        else:
            msg.y = axis.y
            
        self.cmd_vel_pub.publish(msg)

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

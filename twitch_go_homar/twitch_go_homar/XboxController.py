import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from std_msgs.msg import String
from xbox360controller import Xbox360Controller

class XboxController(Node):
    def __init__(self):
        super().__init__('xbox_controller')
        self.cmd_vel_pub = self.create_publisher(Vector3, 'cmd_vel', 10)
        self.servo_pub = self.create_publisher(String, 'servo_cmd', 10)
        self.timer = self.create_timer(0.1, self.publish_joystick_state)
        self.joystick_state = Vector3()
        try:
            self.controller = Xbox360Controller(0, axis_threshold=0.0)
            self.controller.button_a.when_pressed = self.on_button_a_pressed
            self.controller.button_y.when_pressed = self.on_button_y_pressed
            self.controller.axis_l.when_moved = self.update_joystick_state
        except Exception as e:
            self.get_logger().error(f'Exception while init controller: {e}')
        
    def on_button_a_pressed(self, button):
        servo_cmd = String()
        servo_cmd.data = 'up'
        self.servo_pub.publish(servo_cmd)

    def on_button_y_pressed(self, button):
        servo_cmd = String()
        servo_cmd.data = 'down'
        self.servo_pub.publish(servo_cmd)

    def update_joystick_state(self, axis):
        self.joystick_state.x = axis.x
        self.joystick_state.y = axis.y

    def publish_joystick_state(self):
        self.cmd_vel_pub.publish(self.joystick_state)
        
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

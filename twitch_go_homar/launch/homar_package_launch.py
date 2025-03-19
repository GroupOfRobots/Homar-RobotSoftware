from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='twitch_go_homar',
            executable='motor_node',
            name='motor_controller',
        ),
        Node(
            package='twitch_go_homar',
            executable='servo_node',
            name='servo_controller',
        ),
        Node(
            package='twitch_go_homar',
            executable='xbox_node',
            name='xbox_controller',
        )
    ])
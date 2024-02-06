from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='twitch_go_robot',
            namespace='twitch_go_robot',
            executable='motor_node',
            name='motor_node'
        )
    ])
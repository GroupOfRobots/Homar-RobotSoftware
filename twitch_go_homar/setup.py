from setuptools import find_packages, setup
import os

package_name = 'twitch_go_homar'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), ['launch/homar_package_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dn',
    maintainer_email='dawid.nowicki@protonmail.com',  
    description=' package for controlling Homar robot',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_node = twitch_go_homar.MotorController:main',
            'servo_node = twitch_go_homar.ServoController:main',
            'xbox_node = twitch_go_homar.XboxController:main',
        ],
    },
)

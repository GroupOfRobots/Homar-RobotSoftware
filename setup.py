from setuptools import find_packages, setup
import os
from glob import glob

package_name = "twitch_go_robot"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        (os.path.join('share', package_name, "launch"), glob('launch/*.launch.py')),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="mikic202",
    maintainer_email="mikolaj.chomanski@gmail.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["motor_node = twitch_go_robot.MotorNode:main"],
    },
)

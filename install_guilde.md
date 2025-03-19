# Wymagania wstępne
Sprawdź czy ustawione jest zmienne

```
echo $ROS_DISTRO
echo $ROS_PACKAGE_PATH
```
Jeśli ROS_DISTRO nie jest ustawiona 

```
export $ROS_DISTRO=change_me 
```
Jeśli ROS_PACKAGE_PATH nie jest ustawiona 

```
export ROS_PACKAGE_PATH=/opt/ros/$ROS_DISTRO/share:$ROS_PACKAGE_PATH
```

# Instalacja paczki
```
cp twitch_go_homar ~/ros2_ws/src
cd ~/ros2_ws/src
colcon build --packages-select twitch_go_homar
```

# Uruchomienie joy node (https://index.ros.org/p/joy/)

```
sudo apt install ros-$ROS_DISTRO-joy 
ros2 run joy joy_node &
```

# Uruchomienie paczki 

```
ros2 launch twitch_go_homar homar_package_launch.py
```

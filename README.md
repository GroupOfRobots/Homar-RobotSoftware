# Uruchomienie pakietu
> ⚠️ **UWAGA:** Zakłada się, że do Homara podłączony jest pad.
## Aby ręcznie uruchomić pakiet:
```
ros2 launch twich_go_homar  homar_package_launch.py
```

## Dodanie serwisu (autouruchamianie przy starcie) 
1. uruchom edytor plików
```
sudo nano /etc/systemd/system/homar_launcher.service
```
2. Wklej zawartość pliku homar_launcher.service, pamiętając o ustawieniu zmiennej ROS2_WS w poniższej linii:
```
Environment="ROS2_WS=CHANGE_ME"
```
Zamień CHANGE_ME na ścieżkę do katalogu z Twoim workspace'em ROS 2, np. /home/pi/ros2_ws.


3. Zrestartuj systemd i aktywuj serwis:
```
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable homar_launcher.service
sudo systemctl start homar_launcher.service
```

4. Sprawdź, czy serwis działa poprawnie:
```
sudo systemctl status homar_launcher.service
```
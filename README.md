Установка:
1. git clone https://github.com/GearShot77/Raspberry-Pi-receiver-and-transmitter-433MHz-
2. pip3 install rpi-rf

Пример:
 Прием:
 python3 recieve.py -g 20 (raspberry pi pin);
   Отправка:
  python3 send.py -g 21 -t1-p 335 869640

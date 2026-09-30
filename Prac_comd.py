Practical 6
Connection scheme Raspberry Pi
GND  14 
VCC   4 
DI0    18 
CLK   16 

Practical 5
vcc 2
gnd 6
tx 10
sudo apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
sudo systemctl enable serial-getty@ttyAMA0.service
sudo apt-get install minicom
pip install pynmea2 --break-system-packages
sudo cat /dev/ttyS0

Practical 8
CMD commands:
sudo raspi-config (enable i2c)
pip install board --break-system-packages
sudo pip install drawnow --break-system-packages
sudo apt-get install -y i2c-tools python3-smbus
python3 -m pip install --upgrade --no-cache-dir adafruit-blinka adafruit-circuitpython-busdevice adafruit-circuitpython-ads1x15 --break-system-packages
Connection:
ADS1115 Pin	Raspberry Pi Pin Number	Raspberry Pi Function
VDD	Pin 1	3.3V Power
GND	Pin 6	Ground
SDA	Pin 3	GPIO2 (SDA1 – I²C Data)
SCL	Pin 5	GPIO3 (SCL1 – I²C Clock)

Practical 9
Pin 6 GND
Pin 2 VCC
Pin 3 SDA
Pin 5 SCL
Channel 1 On
Channel 2 Off
Enter the following Commands:
Command 1: sudo raspi-config (enable i2c)
Command 2: pip3 install adafruit-circuitpython-pn532 --break-system-packages
Command:
Command 1: sudo raspi-config (enable i2c)
Command 2: sudo reboot
Command 3: pip3 install adafruit-circuitpython-pn532 --break-system-packages
Command 3: sudo apt install -y libnfc-bin libnfc-dev libusb-dev libpcsclite-dev i2c-tools
Command 4: sudo nano /etc/nfc/libnfc.conf
changes in config file:
allow_autoscan = false
device.name = "PN532 over I2C"
device.connstring = "pn532_i2c:/dev/i2c-1"
save.
Command 5: i2cdetect –y 1 (optional put sudo)
Command 6: nfc-list
import subprocess
import time

NAME = "Priya"
last_uid = None

try:
    while True:
        output = subprocess.getoutput("nfc-list")

        if "UID" in output:
            for line in output.splitlines():
                if "UID" in line:
                    uid = line.split(":")[1].strip().replace(" ", "")

                    if uid != last_uid:
                        print(f"{NAME}: {uid}")
                        last_uid = uid
                    break

        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopped")

Practical 10
#pip3 install pyfingerprint
/pyfingerprint/src/files/pyfingerprint
sudo python pyfingerprint.py

VCC Red
GND Black
Tx Yellow
Rx White


Practical 7
Gnd   6
Vcc    2
Ini      26

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from time import sleep

relay_pin1=26
relay_pin2=24
relay_pin3=21
relay_pin4=20

GPIO.setmode(GPIO.BOARD)

GPIO.setup(relay_pin1,GPIO.OUT)
GPIO.setup(relay_pin2,GPIO.OUT)
GPIO.setup(relay_pin3,GPIO.OUT)
GPIO.setup(relay_pin4,GPIO.OUT)

GPIO.output(relay_pin1,1)
GPIO.output(relay_pin2,1)
GPIO.output(relay_pin3,1)
GPIO.output(relay_pin4,1)

try:
    while True:
        GPIO.output(relay_pin1,0)
        sleep(5)
        GPIO.output(relay_pin2,0)
        sleep(5)
        GPIO.output(relay_pin3,0)
        sleep(5)
        GPIO.output(relay_pin4,0)
        sleep(5)

        GPIO.output(relay_pin1,1)
        sleep(5)
        GPIO.output(relay_pin2,1)
        sleep(5)
        GPIO.output(relay_pin3,1)
        sleep(5)
        GPIO.output(relay_pin4,1)
        sleep(5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

Practical 3
sudo apt-get install python-pip
source myenv/bin/activate
pip install teleport
git clone https://github.com/salmanfarisvp/TelegramBot.git
cd TelegramBot
nano telegrambot.py
bot = telepot.Bot(‘your_bot_token’)
then run the code

Practical 2
Sudo raspi-cofig
Sudo reboot
libcamera-hello
libcamera-still -o image.jpglibcamera-still -o image.jpg


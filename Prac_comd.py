Practical 6
Connection scheme Raspberry Pi
GND Ground 14 GND
VCC +5V Power 4 5V
DI0 Data In 18 GPIO 24
CLK        16 

Practical 5
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
Enter the following Commands:
Command 1: sudo raspi-config (enable i2c)
Command 2: pip3 install adafruit-circuitpython-pn532 --break-system-packages
Command:
Command 1: sudo raspi-config (enable i2c)
Command 2: sudo reboot
Command 3: pip3 install adafruit-circuitpython-pn532 --break-system-packages
Command 3: sudo apt install -y libnfc-bin libnfc-dev libusb-dev libpcsclite-dev i2c-tools
Command 4: sudo nano /etc/nfc/libnfc.conf

Practical 10
#pip3 install pyfingerprint

Practical 7
Gnd   6
Vcc    2
Ini      26

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


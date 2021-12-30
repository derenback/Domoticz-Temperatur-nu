# Domoticz-Temperatur-nu
This is a plugin for Domoticz that will get temperature data from the website temperature.nu
A list of avilable measurement locations can be found here: www.temperatur.nu/matplatser

## Installation
```bash
cd ~/domoticz/plugins
git clone https://github.com/derenback/Domoticz-Temperatur-nu.git
sudo systemctl restart domoticz
```
- Make sure to have the setting "Accept new Hardware Devices" turned on for new devices to be added when adding the Hardware in domoticz.

## Update
```bash
cd ~/domoticz/plugins/Domoticz-Temperatur-nu
git pull
sudo systemctl restart domoticz
```

## Tested on
- Domoticz version: 2020.2 (build 11997)


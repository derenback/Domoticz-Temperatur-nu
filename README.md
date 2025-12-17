# Domoticz-Temperatur-nu

A [Domoticz](https://www.domoticz.com/) plugin that retrieves temperature data from [temperatur.nu](https://www.temperatur.nu/) - a Swedish network of weather stations providing real-time temperature readings.

## Features

- Fetches temperature data from multiple Swedish locations
- Creates temperature sensor devices automatically in Domoticz
- Updates every 5 minutes
- Debug mode for troubleshooting

## Requirements

- Domoticz 2024.7 or later
- Python 3.x
- `requests` library (install with `pip install requests`)

## Installation

```bash
cd ~/domoticz/plugins
git clone https://github.com/derenback/Domoticz-Temperatur-nu.git
pip install requests
sudo systemctl restart domoticz
```

> **Note:** Make sure the setting "Accept new Hardware Devices" is turned on in Domoticz (Setup → Settings → System) for new devices to be created automatically.

## Configuration

1. Go to **Setup → Hardware** in Domoticz
2. Select **Temperature.nu** from the Type dropdown
3. Enter your desired locations separated by commas (e.g., `mosas,salen_by`)
4. Click **Add**

### Finding Location Names

A list of available measurement locations can be found at: [www.temperatur.nu/matplatser](https://www.temperatur.nu/matplatser)

> **Important:** Adding many locations may violate the [terms of service](https://www.temperatur.nu/). Please use responsibly.

## Update

```bash
cd ~/domoticz/plugins/Domoticz-Temperatur-nu
git pull
sudo systemctl restart domoticz
```

## Troubleshooting

- **No devices created:** Ensure "Accept new Hardware Devices" is enabled
- **No temperature updates:** Enable Debug mode in the hardware settings to see detailed logs
- **Connection errors:** Check your internet connection and that temperatur.nu is accessible

## License

See [LICENSE](LICENSE) file.

## Tested On

- Domoticz version: 2024.7


---

# OpenWeather CLI

Quick CLI application I made to interface with the openweather API for use in waybar.
Weather CLI is a simple command line application that fetches and displays weather data. It uses the OpenWeatherMap API and can be customized via a configuration file. 

## Features

- Get the current weather for any location
- Choose between Celsius, Fahrenheit, or Kelvin temperature scales
- Select the output format: either in a single line or multiple lines
- Customize the output: show or hide labels, set the width between printed items, and add specific text or symbols before and after each entry

## Installation

There are two ways to install OpenWeather CLI:

### 1. From PyPi

You can install OpenWeather CLI from PyPi using pip:

```bash
pip install openweather-cli
```

Once installed, you can run the application with:

```bash
openweather-cli
```

### 2. From Source (GitHub)

First, clone the repository:

```bash
git clone https://github.com/username/openweather-cli.git
cd openweather-cli
```

Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application with:

```bash
python -m openweather-cli.main
```

## Configuration

You can customize the behavior of the Weather CLI by editing the `config.json` file located in `~/.config/weather_cli/`. Here's an example of the configuration:

```json
{
    "api_key": "your_api_key_here",
    "location": "your_location_here",
    "output_format": "single_line",
    "temperature_unit": "celsius",
    "print_options": ["temperature", "description"],
    "enable_labels": false,
    "separation_width": 5,
    "pre_text": "[",
    "post_text": "]"
}
```

- `api_key`: Your OpenWeatherMap API key.
- `location`: The location for which you want to fetch the weather.
- `output_format`: Can be `single_line` or `multi_line`. Determines whether the output is printed in a single line or on multiple lines.
- `temperature_unit`: Can be `celsius`, `fahrenheit`, or `kelvin`.
- `print_options`: An array of the elements you want to print. Can include `weather`, `temperature`, and `description`.
- `enable_labels`: Boolean value indicating whether to print labels (Weather, Temperature, Description) before each data item.
- `separation_width`: The number of spaces between each printed item.
- `pre_text`: A text or symbol to add before each data item.
- `post_text`: A text or symbol to add after each data item.

Please note that you need to replace `your_api_key_here` with your actual OpenWeatherMap API key and `your_location_here` with the actual location for which you want to fetch the weather.

## License

MIT

---

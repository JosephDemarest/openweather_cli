import json
import os

def read_config():
    home_dir = os.path.expanduser("~")
    config_path = os.path.join(home_dir, ".config/weather_cli/config.json")
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

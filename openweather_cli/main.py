from weather_cli import config, weather

def main():
    config_data = config.read_config()
    weather_data = weather.fetch_weather_data(config_data['api_key'], config_data['location'], config_data['temperature_unit'])
    weather.parse_and_output(weather_data, 
                             config_data['output_format'], 
                             config_data['print_options'],
                             config_data['enable_labels'],
                             config_data['separation_width'],
                             config_data['pre_text'],
                             config_data['post_text'])

if __name__ == "__main__":
    main()

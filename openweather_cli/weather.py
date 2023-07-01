import requests
import json

def fetch_weather_data(api_key, location, unit):
    unit_param = 'metric' if unit == 'celsius' else 'imperial' if unit == 'fahrenheit' else 'standard'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units={unit_param}')
    data = json.loads(response.text)
    return data


def parse_and_output(data, format, print_options, enable_labels, separation_width, pre_text, post_text):
    main_weather = data['weather'][0]['main'] if 'weather' in print_options else None
    description = data['weather'][0]['description'] if 'description' in print_options else None
    temp = data['main']['temp'] if 'temperature' in print_options else None

    label = lambda text, label: f"{label}: {text}" if enable_labels else f"{text}"
    separate = lambda text: f"{pre_text}{text}{post_text}".ljust(separation_width)

    if format == 'single_line':
        output = " ".join(filter(None, [
            separate(label(main_weather, "Weather")) if main_weather else "",
            separate(label(description, "Description")) if description else "",
            separate(label(temp, "Temperature")) if temp else ""
        ]))
        print(output.strip())
    else:
        if main_weather:
            print(separate(label(main_weather, "Weather")))
        if description:
            print(separate(label(description, "Description")))
        if temp:
            print(separate(label(temp, "Temperature")))

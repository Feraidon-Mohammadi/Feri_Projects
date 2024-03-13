import requests




api_key = "242ceb287911820333677345279f9b9a"


city = "erfurt"
state = "thuringen"
country = "de"

api_all_call = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&cnt=16&appid={api_key}"

response = requests.get(api_all_call)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)



"""
infos value : 
This is the response from the OpenWeatherMap API for the city of Erfurt in Germany. Let's break down some of the key information:

coord: Coordinates of the location (longitude: 11.0333, latitude: 50.9833).
weather: Information about the current weather conditions, which include:
id: Weather condition ID.
main: Main weather condition (e.g., 'Clouds').
description: Description of the weather condition (e.g., 'few clouds').
icon: Weather icon code.
base: Data source (in this case, 'stations').
main: Main weather information, including:
temp: Current temperature in Kelvin (284.34 K).
feels_like: Apparent ("feels like") temperature in Kelvin (283.47 K).
temp_min: Minimum temperature in Kelvin (282.84 K).
temp_max: Maximum temperature in Kelvin (285.24 K).
pressure: Atmospheric pressure in hPa (1009 hPa).
humidity: Relative humidity in percentage (75%).
visibility: Visibility in meters (10000 meters).
wind: Wind information, including:
speed: Wind speed in meter/second (6.17 m/s).
deg: Wind direction in degrees (240 degrees).
clouds: Cloudiness information, including:
all: Cloudiness percentage (20%).
dt: Time of data calculation, UNIX timestamp (1700475182).
sys: System information, including:
type: System type (1).
id: System ID (1266).
country: Country code (DE for Germany).
sunrise: Sunrise time, UNIX timestamp (1700462381).
sunset: Sunset time, UNIX timestamp (1700493804).
timezone: Timezone offset in seconds (3600 seconds or UTC+1).
id: City ID (2929670).
name: City name (Erfurt).
cod: Response code (200 indicates success).

"""
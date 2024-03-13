import requests

# if need webaddress is here
# https://openweathermap.org/current


api_key1 = "242ceb287911820333677345279f9b9a"
lan = "51.16"
lon = "10.45"

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lan}&lon={lon}&exclude=daily&appid={api_key1}"

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)

# output = {
#          'coord': {'lon': 10.45, 'lat': 51.16},
#          'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}],
#          'base': 'stations',
#          'main': {'temp': 283.96, 'feels_like': 283.37, 'temp_min': 283.28, 'temp_max': 285.51, 'pressure': 1008, 'humidity': 87, 'sea_level': 1008, 'grnd_level': 984},
#          'visibility': 10000,
#          'wind': {'speed': 7.12, 'deg': 253, 'gust': 11.8},
#          'clouds': {'all': 91},
#          'dt': 1700480661,
#          'sys': {'type': 2, 'id': 2000152, 'country': 'DE', 'sunrise': 1700462562,'sunset': 1700493903},
#          'timezone': 3600,
#          'id': 2863516,
#          'name': 'Niederdorla',
#          'cod': 200}

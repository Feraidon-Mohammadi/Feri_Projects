import requests

# beautiful Json format website : https://jsonviewer.stack.hu/


url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "242ceb287911820333677345279f9b9a"
api_key2 = "7f427350474c1ca6f47b1b1012dc9457"

weather_params = {
    "lat":51.16,
    "lon":10.45,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(url, params=weather_params)

#if response.status_code == 200:
#print(response.json())
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)


weather_data = response.json()
print(f"Here are all data: {weather_data["weather"]}\n")
print(f"Here is what u exactly -> weatherid: {weather_data["weather"][0]["id"]}")
print(f"Today's wind speed : {weather_data["wind"]["speed"]} km/h")




############################### Temperature ###########################################
today_temperature = weather_data["main"]["temp"]
print(f"Today's Temperature: {today_temperature} K")

# Convert Kelvin to Celsius
today_temperature_celsius = today_temperature - 273.15
print(f"Today's Temperature: {today_temperature_celsius:.2f} °C")

# Convert Kelvin to Fahrenheit
today_temperature_fahrenheit = (today_temperature - 273.15) * 9/5 + 32
print(f"Today's Temperature: {today_temperature_fahrenheit:.2f} °F")




# Assuming weather_data is your dictionary containing the weather information
weather_conditions = weather_data["weather"]
if weather_conditions:
    main_condition = weather_conditions[0]["main"]
    description = weather_conditions[0]["description"]
    print(f"Main Weather Condition: {main_condition}")
    print(f"Description: {description}")
else:
    print("No weather information available.")





###################################################################################
#  its correct but need to subscribe to use this , just for know i added how to get some values in aloop with limit
# weather_slice = f"Here are all data2: {weather_data["weather"][:6]}" # from 0 to 6 we need min and max value that we need
# print(weather_slice)
#
# will_rain = False
# for hourly_data in weather_slice:
#     condition_cod = hourly_data["weather"][0]["id"]
#     if int(condition_cod) < 700:
#         will_rain = True
#
# if will_rain:
#     print("bring an umbrella")
#####################################################################################




# the values will be liek this - i added to better understanding
weater_data_values ={
                    'coord':{'lon':10.45,
                             'lat':51.16},

                    'weather':[{'id':802,
                                'main':'Clouds',
                                'description':'scattered clouds',
                                'icon':'03d'}],

                    'base':'stations',
                    'main':{'temp':284.38,
                            'feels_like':283.8,
                            'temp_min':283.83,
                            'temp_max':284.87,
                            'pressure':1008,
                            'humidity':86,
                            'sea_level':1008,
                            'grnd_level':984},

                    'visibility':10000,
                    'wind':{'speed':7.24,
                            'deg':249,
                            'gust':11.17},

                    'clouds':{'all':30},
                    'dt':1700484846,
                    'sys':{'type':2,
                           'id':2000152,
                           'country':'DE',
                           'sunrise':1700462562,
                           'sunset':1700493903},

                    'timezone':3600,
                    'id':2863516,
                    'name':'Niederdorla',
                    'cod':200
                    }


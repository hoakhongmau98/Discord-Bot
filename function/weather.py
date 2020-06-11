# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests
import json


def weather(city_name):
    # Enter your API key here
    api_key = "d7fb6928448a9df3527ff57926ebec3c"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name
    # city_name = input("Enter city name : ")

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
        # store the value corresponding
        # to the "humidity" key of y
        current_humidiy = y["humidity"]
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
        # print following values
        info = " Temperature (in Celsius unit) = "+str(current_temperature-273.15)+" *C"\
               + "\n Feels like: " + str(y['feels_like']-273.15)+" *C"+"\nTemperature max/min: "+str(y['temp_max']-273.15)+"/"\
               + str(y['temp_min']-273.15)+" *C"+"\natmospheric pressure (in hPa unit) = "\
               + str(current_pressure)+"\n humidity (in percentage) = "+str(current_humidiy)+"%"+"\n description = "\
               + str(weather_description)
        return info
    else:
        return 'City not found'

# a = {'coord': {'lon': 105.84, 'lat': 21.02},
#      'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}],
#      'base': 'stations',
#      'main': {'temp': 294.15, 'feels_like': 296.79, 'temp_min': 294.15, 'temp_max': 294.15, 'pressure': 1016, 'humidity': 94},
#      'visibility': 2100,
#      'wind': {'speed': 1.5, 'deg': 40},
#      'clouds': {'all': 90},
#      'dt': 1584378298,
#      'sys': {'type': 1, 'id': 9308, 'country': 'VN', 'sunrise': 1584399805, 'sunset': 1584443196},
#      'timezone': 25200,
#      'id': 1581130,
#      'name': 'Hanoi',
#      'cod': 200}

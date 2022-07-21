# File: DSC510_10.2.v4
# Name: Ryan P Long
# Assignment Number 10.2
# Date: 08/04/19
# Desc:  User selects either zip code, city, or stops the program. Next prompt
#        asks user to input either zip or city, program then checks format. Then
#        requests weather data from OpenWeatherMap.org using API request and
#        displays pertinent weather in readable format. Request function also
#        checks the connection to OpenWeatherMap.org. User than can either repeat
#        or stop the program.
#
# Usage: Select either zip code, city, or stop. Input either zip or city, can be
#        repeated until stopped by user.

import requests
import pytemperature


# Validates user input of zip code
def zipcodechecker():
    zipenter = input('Type a 5 digit zip code: ')
    if len(zipenter) != 5 or (not zipenter.isdigit()):
        print('Enter only 5 digits')
    else:
        zipcodegetter(zipenter)


# Validates user input of city
def citynamechecker():
    cityenter = input('Enter a city name: ')
    if any(char.isdigit() for char in cityenter):
        print('Enter only letters')
    else:
        citynamegetter(cityenter)


# Requests data from API if zip code is the input, checks request/connection
def zipcodegetter(a):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    querystring = {'zip': a,
                   'APPID': 'd4dbe8513fac6ef3d0d4ebfac721d4cf'}
    headers = {'cache-control': 'no-cache'}

    try:
        response = requests.request('GET', url, headers=headers, params=querystring)
        zipweather = response.json()
        weatherprinter(zipweather)
    except requests.exceptions.RequestException:
        print('Connection is not working')


# Requests data from API if city is the input, checks request/connection
def citynamegetter(b):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    querystring = {'q': b,
                   'APPID': 'd4dbe8513fac6ef3d0d4ebfac721d4cf'}
    headers = {'cache-control': 'no-cache'}
    try:
        response = requests.request('GET', url, headers=headers, params=querystring)
        zipweather = response.json()
        weatherprinter(zipweather)
    except requests.exceptions.RequestException:
        print('Connection is not working')


# Validates received request & prints in readable format. Converts Kelvin to Celsius & Fahrenheit
# and m/s to mph.
def weatherprinter(c):
    try:
        weather_str = c['main']
        descript_str = c['weather']
        wind_str = c['wind']

        city_name = c['name']
        description = descript_str[0]['description']
        temperature = weather_str['temp']
        wind = wind_str['speed']
        humidity = weather_str['humidity']
        pressure = weather_str['pressure']

        print('\nCurrent weather for:', city_name)
        print('Description: ', description.capitalize())
        print('Temperature (°C/°F): ', round(pytemperature.k2c(temperature)),
              '/', round(pytemperature.k2f(temperature)))
        print('Wind (mph): ', round(wind*2.23694, 1))
        print('Humidity (%): ', humidity)
        print('Atmospheric Pressure (hpa): ', pressure)
    except KeyError:
        print('Location does not exist')


# Main function for entry
def main():
    looping = True
    while looping:
        selection = input('\nFor the weather enter: (z)ip code, (c)ity name, or (s)top: ')
        if selection == 's':
            print('\nThanks for using!')
            looping = False
        elif selection == 'z':
            zipcodechecker()
        elif selection == 'c':
            citynamechecker()
        else:
            print('Entry needs to be: z, c, s')


if __name__ == '__main__':
    print('\nWelcome!')
    main()

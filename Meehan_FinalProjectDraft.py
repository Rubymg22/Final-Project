import json
import requests

print('Welcome to the weather forecast data app!')

while True:

    location = input(' Please enter either a Zip Code or City Name: ')

    if location.isdigit():
        key = f"zip={location}"
    else:
        key = f'q={location}'

    url = 'http://api.openweathermap.org/data/2.5/weather?' + key + ",US" + '&appid=1cf0ada9484bcf82137cae42d7105d75'
    print(url)

    print("Requesting Connection")
    request = requests.get(url)

    try:
        print('Successful Connection')

        data = json.loads(request.text)

        print('Weather Data:')
        print('City of', data['name'])
        print('Temperature:', data['main']['temp'] * 9/5 - 459.67, 'fahrenheit')
        print('Weather:', data['weather'][0]['description'])
        print('Wind Speed:', data['wind']['speed'] * 1.943844, 'knots')
        print('Pressure:', data['main']['pressure'], 'mb')
        print('Humidity:', data['main']['humidity'], '%')
        print('Coordinates:', data['coord'])
    except:
        print("City does no exist, please try again.")
import requests  # imports the requests library
import json  # imports the json library

# prints a welcome message
print('Welcome to the weather forecast data app!')

while True:  # this allows the program to continue looping while all if this code is true

    # This will get the user input for the Zip code or City name
    location = input(' Please enter either a Zip Code or City Name: ')


    if location.isdigit():  # If the user inputs a zip code, then python will choose this key
        key = f"zip={location}"
    else:  # If the user types anything else, then python will choose this key
        key = f'q={location}'

    # This is the url variable that python will use to pull from the webservice.
    url = 'http://api.openweathermap.org/data/2.5/weather?' + key + ",US" + '&appid=1cf0ada9484bcf82137cae42d7105d75'
    print(url)  # This will print the variable to the user.

    print("Requesting Connection")  # So the user knows python is requesting a connection.
    request = requests.get(url)  # This send a GET response to the url variable from above.

    try:  # If we get a response back, then python will choose this block.
        print('Successful Connection')  # This will be printed if the connection is successful.

        # This will read the JSON data from the webservice and turn it into a dictionary.
        data = json.loads(request.text)

        # These next few lines will print all of the Weather Data from the Webservice dictionary.
        print('Weather Data:')
        print('City of', data['name'])
        print('Temperature:', data['main']['temp'] * 9/5 - 459.67, 'fahrenheit')
        print('Weather:', data['weather'][0]['description'])
        print('Wind Speed:', data['wind']['speed'] * 1.943844, 'knots')
        print('Pressure:', data['main']['pressure'], 'mb')
        print('Humidity:', data['main']['humidity'], '%')
        print('Coordinates:', data['coord'])
    except:  # If python does not get a valid response back from the server, then it will use this block.
        print("City does no exist, please try again.")  # Tells the user to try again.

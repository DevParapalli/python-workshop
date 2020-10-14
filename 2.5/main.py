import requests
import pprint
# take input from user for the city
data = {
    'q':input("Enter City Name:") or 'Nagpur',
    'appid':'6b677150cf4163824cc11d79a20b6aff',
    'units':'metric'
}
r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=data)
pprint.pprint(r.json()['name'])
pprint.pprint(r.json()['main'])
pprint.pprint(r.json()['weather'][0])
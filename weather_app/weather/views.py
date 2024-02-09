from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=e8357335b1fe06fdc1b38ee8e4046636').read()

        list_of_data = json.loads(source)

        data = {
            "name": str(list_of_data['name']),
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + "," + str(list_of_data['coord']['lat']),

            "temp_now": str(list_of_data['main']['temp'] - 273.15),
            "feels_like": str(list_of_data['main']['feels_like'] - 273.15),
            "temp_min": str(list_of_data['main']['temp_min'] - 273.15),
            "temp_max": str(list_of_data['main']['temp_max'] - 273.15),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),

            "wind_speed": str(list_of_data['wind']['speed']),
            "weather_main": str(list_of_data['weather'][0]['description']),
        }
        print(data)
    else:
        data = {
            "not_found": "OOps, the city have you entered was not found",
        }
        print(data)

    return render(request, 'weather/index.html', data)
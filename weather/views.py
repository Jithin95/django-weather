from django.shortcuts import render
import requests
from .models import City

def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=214f82430c1f8d8606f604177400a16c"
    weather_city = []
    cities = City.objects.all()
    for city in cities:
        r = requests.get(url.format(city.city_name)).json()
        city_weather = {
            'city_name': city.city_name,
            'city_temp': r['main']['temp'],
            'weather_desc': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_city.append(city_weather)
    context = {'city_weather': weather_city}
    return render(request, 'weather/index.html', context)

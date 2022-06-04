from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

import requests
from .models import location
from .forms import CityForm
#from decouple import config

#APPID = config('271d1234d3f497eed5b1d80a07b3fcd1')


# Create your views here.
def Homeview(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    error_message = ''
    message = ''
    message_class = ''

    if request.method == "POST":
        form = CityForm(request.POST)

        if form.is_valid():

            new_city = form.cleaned_data['name']
            existing_city_count = location.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                api_response = requests.get(url.format(new_city)).json()

                if api_response['cod'] == 200:
                    form.save()
                else:
                    error_message = 'Invalid city name!!! Try again!!'
            else:
                error_message = 'City already exists on the Page'

        if error_message:
            message = error_message
            message_class = 'is-danger'
        else:
            message = "City added succesfully !!"
            message_class = 'is-success'

    form = CityForm()

    cities = location.objects.all().order_by('-id')

    weather_list = []

    for city in cities:
        api_response = requests.get(url.format(city)).json()
        city_weather = {
            'city': city,
            'temperature': (int(api_response['main']['temp'] -32)*.55),
            'description': api_response['weather'][0]['description'],
            'icon': api_response['weather'][0]['icon'],
        }
        weather_list.append(city_weather)

    context = {
        'weather_list': weather_list,
        'form': form,
        'message': message,
        'message_class': message_class
    }
    return render(request, 'HTML/home.html', context)


def DeleteCityView(request, city_name):
    city = location.objects.filter(name=city_name)
    city.delete()

    return redirect('home')
import copy

from django.shortcuts import render

from django.shortcuts import render
import urllib.request
import json
import matplotlib.pyplot as plt
# import wheel
# import pandas as pd
from copy import deepcopy
# Create your views here.
def home(request):
    if request.method == 'POST':

        city = request.POST['city']
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=cd4415a99345841edbb9040348e3f2d6').read()

        # convert  json file into python dectionary
        list_of_data = json.loads(source)

        data = {
            'country_code': str(list_of_data['sys']['country']),
            'cor': str(list_of_data["coord"]["lon"]) + " " + str(list_of_data["coord"]["lat"]),
            'temp': str(list_of_data["main"]['temp']),
            'pressure': str(list_of_data['main']["pressure"]),
            'humidity': str(list_of_data['main']['humidity']),
            'main': str(list_of_data["weather"][0]['main']),
            'description': str(list_of_data["weather"][0]['description']),
            'icon': list_of_data["weather"][0]['icon'],
            'city': city
        }

        tupl=("country_code",'cor','description','icon','city')
        data1=copy.deepcopy(data)
        for i in tupl:
            data1.pop(i)
        lst1=data1.keys()
        lst2=data1.values()
        #df=pd.DataFrame(list(data1.items(),columns=["features","values"]))
        fig=plt.figure(figsize=(10,6))
        # plt.bar(df["features"],df["values"])
        plt.bar(lst1,lst2)
        plt.title(str(city))
        fig.savefig("output_fig.jpg")

    else:
        data = {}


    return render(request, 'weather.html', data)
# Create your views here.

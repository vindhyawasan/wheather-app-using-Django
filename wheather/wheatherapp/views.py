from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def wheather(request):

    if request.method == 'POST':
        search = request.POST.get('search')
        API_KEY = "b73e2da15783ad61f250af2757175b64"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={search}&appid={API_KEY}"

        data = requests.get(url).json()
        # print(data) 
        return render(request,"index.html",{"data":data})
    return render(request,"index.html")

# Create your views here.

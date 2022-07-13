import json  
from django.shortcuts import render  
import urllib.request  
import json  

def main(request):  
    if request.method == 'POST': 
        city = request.POST.get('city', 'True')  
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=9633bbe3f8087deb59fab4157da11a28').read()  
        list_of_data = json.loads(source)  
        context = {  
            'city': city, 
            "pressure": str(list_of_data['main']['pressure']),  
            "humidity": str(list_of_data['main']['humidity']),   
            "country_code": str(list_of_data['sys']['country']),  
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),  
            "temp": str(list_of_data['main']['temp']) + ' K',  
        }  
    else:  
        context = {}  
    return render(request, 'index.html', context)  
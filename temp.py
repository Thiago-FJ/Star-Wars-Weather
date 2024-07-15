import requests



def convert_temp(temp_kelvin):
    temp_celsius = temp_kelvin-273
    #temp_fahrenheit = (temp_celsius*1.8)+32
    return temp_celsius #, temp_fahrenheit

def init(city):
    KEY = open('KeyClima','r').read()
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = city
    return BASE_URL + "appid=" + KEY + "&q=" + CITY 

city = "Liberia"
url = init(city)
response = requests.get(url).json()

temp = convert_temp(response['main']['temp'])
clime = response['weather'][0]['main'].lower()
humidade = response['main']['humidity']

if (clime == "clouds") and (response['weather'][0]['id']==801):
    clime = "clear"


#print(f"A temperatura na cidade: {city} é de {temp:.1f}°C\nParece que está {clime}")
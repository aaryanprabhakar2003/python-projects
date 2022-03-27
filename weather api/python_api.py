import requests
import json
api_key = "5a2f9ebccdba43171f7b44aacb77c957"
url = "http://api.openweathermap.org/data/2.5/weather?q=India&appid=5a2f9ebccdba43171f7b44aacb77c957"
response = requests.get(url)
print("Response Code: ",response.status_code)
data = json.loads(response.text)
main=data['main']
temperature = main['temp']
coord=data['coord']
lon=coord['lon']
lat=coord['lat']
print("Current Longitude is:",lon)
print("Current Latitude is: ",lat)
temp_min=main['temp_min']
temp_max=main['temp_max']
humidity=main["humidity"]
print("Current Temperature is:",temperature)
print("Maximum Temperature is: ",temp_max)
print("Minimum Temperature is: ",temp_min)
print("Current Humidity is: ",humidity)

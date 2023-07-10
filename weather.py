#weather forecast
import requests
city=input("Please enter the city to know the temperature : ")
response = requests.get('http://api.weatherapi.com/v1/current.json?key=051b9636b62b4866a81140703230607&q='+city+'&aqi=no')
json_response = response.json()
description=json_response.get('current').get('condition').get('text')
curr_temp=json_response.get('current').get('temp_c')
print("Today's weather in",city,"city is",description,"and",curr_temp,"degrees celsius")
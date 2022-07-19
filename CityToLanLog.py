import requests
import json

city = str(input("Enter city: "))
url = "https://api.geocodify.com/v2/geocode?api_key=a887f9469560d73c6aee997a657c41115a5d2c33&q=" + city
response = requests.get(url).content
json_data = json.loads(response)
name = json_data["response"]["features"][0]["properties"]["name"]
lon, lat = json_data["response"]["features"][0]["geometry"]["coordinates"]

print("The latitude and longitude of the city '{}' are : ".format(name))
print("Latitude : {}, Longitude : {}".format(lat,lon))
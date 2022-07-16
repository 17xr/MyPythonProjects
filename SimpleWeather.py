import json
import requests

print("A simple weather app! made by ❤ from @17xr")
print()

def weather_json(url):
    data = requests.get(url)
    return data.json()

def weather_data(json_file: json):
    name = json_file['location']['name']
    weather = json_file['current']['condition']['text']
    temperature = json_file['current']['temp_c']
    wind_speed = json_file['current']['wind_kph']
    country = json_file['location']['country']
    return name, country, weather, temperature, wind_speed

def main():
    try:
        city = str(input("Enter the name of the city: "))
    except:
        print("Please enter a valid city name...")
        input("Press a key to exit...")
        exit()
    api_url = "https://api.weatherapi.com/v1/current.json?key=354a28c9dc4d4a3282e233542221507&q=" + city
    try:
        response = weather_json(api_url)
        data = weather_data(response)
    except:
        print("There was an error, Sorry!")
        input("Press a key to exit...")
        exit()
    print("The city: {} ,{}. The weather feels like: {}.".format(data[0],data[1],data[2]))
    print("The temperature is {}°C, The wind speed is {} Km/h.".format(data[3],data[4]))
    print()
    check = str(input("Would you like to check the weather for another city ? (Yes/No): "))
    print()
    if check in ['yes','YES','Yes','y','Y']:
        main()
    else:
        input("Press a key to exit...")
        exit()

if __name__ == '__main__':
    main()
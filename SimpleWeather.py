import json
import requests

print("A simple weather app! made by ❤ from @17xr")
print()

def weather_json(url):
    data = requests.get(url)
    return data.json()

def weather_data(json_file: json):
    name = json_file['name']
    weather = json_file['weather'][0]['main']
    temperature = json_file['main']['temp']
    wind_speed = json_file['wind']['speed']
    weather_desc = json_file['weather'][0]['description']
    return name, weather, temperature, wind_speed, weather_desc, weather_desc

def main():
    try:
        city = str(input("Enter the name of the city: "))
    except:
        print("Please enter a valid city name...")
        input("Press a key to exit...")
        exit()
    api_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city +" &units=metric&appid=05ea5487265eaed28c0b052d541c43a1"
    try:
        response = weather_json(api_url)
        data = weather_data(response)
    except:
        print("There was an error, Sorry!")
        input("Press a key to exit...")
        exit()
    print("The city: {} , the weather is : {}.".format(data[0],data[1]))
    print("The temperature is {}°C, The wind speed is {} Km/h.".format(data[2],data[3]))
    print("The weather is decribed as : {}.".format(data[4]))
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
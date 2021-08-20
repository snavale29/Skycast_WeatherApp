# import the reuests library
import requests
from pprint import pprint


# variable declarations
#tkinter._test()


apiKey = "e86405617914e4a6f49f27fb113b402a"
city = input("Enter your city: ")

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=e86405617914e4a6f49f27fb113b402a&units=imperial'.format(city)

res = requests.get(url)

data = res.json()

temp = data['main']['temp']
feelsLike = data['main']['feels_like']
description = data['weather'][0]['description']

print("The current temperature in "+city+" is: ")
print("Temperature: "+str(temp)+" degrees F")
print("Feels Like: "+str(feelsLike)+" degrees F")
print("Description: "+description)

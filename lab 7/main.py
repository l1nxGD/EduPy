from json import loads
import random
import requests

apiKey = "5c0e6a096ab232d92dc3890fe8a59a3e"

cityName = 'Санкт Петербург'

r = requests.post(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}")
data = loads(r.text)

print(f"Сейчас в {cityName}:\n"
      f"Температура: {round(data['main']['temp'] - 273.15, 2)} c\n"
      f"Влажность: {data['main']['humidity']}%\n"
      f"Давление: {data['main']['pressure']} Pa\n")

print(data)

r = requests.get(f'https://rickandmortyapi.com/api/character/{random.randint(1, 826)}')
data = loads(r.text)

print(f"id: {data['id']}:\n"
      f"Имя: {data['name']}\n"
      f"Ориджин: {data['origin']['name']}\n"
      f"Место появления: {data['location']['name']}\n"
      f"Status: {data['status']}\n"
      f"Серия: {data['episode'][0].split('/')[-1]}\n")

print(data)

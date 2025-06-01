import random
import requests

url = "https://rickandmortyapi.com/api/"
response = requests.get(url)
print(response.json())
print()

print("Случайный персонаж из всех")
url = f"https://rickandmortyapi.com/api/character/{random.randint(1, 826)}"
response = requests.get(url)
print(response.json())
print()

print("Персонаж по имени")
url = f"https://rickandmortyapi.com/api/character/?name=pickle"
response = requests.get(url)
print(response.json())
print()

print("Персонаж, содержащий в имени rick вида неизвестный")
url = f"https://rickandmortyapi.com/api/character/?name=rick&'species': 'unknown'"
response = requests.get(url)
print(response.json())
print()

print("Случайная локация из всех")
url = f"https://rickandmortyapi.com/api/location/{random.randint(1, 126)}"
response = requests.get(url)
print(response.json())
print()

print("Локация типа планета ")
url = f"https://rickandmortyapi.com/api/location/?type=planet"
response = requests.get(url)
print(response.json())
print()

print("Последний эпизод, 51-ый")
url = f"https://rickandmortyapi.com/api/episode/51"
response = requests.get(url)
print(response.json())
print()

print("Эпизоды пятого сезона:")
url = f"https://rickandmortyapi.com/api/episode/?episode=S05"
response = requests.get(url)
data = response.json()['results']
for i in data:
    print(i['name'])

import requests
import keyboard

appid = "551710b00fc2be711ffb07c6cae72e92"

while True:
    try:
        city_name = input('Введите название города: ')
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': city_name, 'units': 'metric', 'lang': 'ru', 'appid': appid})
        data = res.json()
        weather = "Погодные условия: " + str(data['weather'][0]['description'])
        temperature = "Температура: " + str(data['main']['temp']) + '°C'
        humidity = "Влажность воздуха: " + str(data['main']['humidity']) + '%'
        pressure = "Давление: " + str(data['main']['pressure']) + ' hPa'
        print(weather + '\n' + temperature + '\n' + humidity + '\n' + pressure + '\n' +
            'Для выхода нажмите ESC, иначе - пробел' + '\n')
        if keyboard.read_key() == 'esc':
            break
        elif keyboard.read_key() == ' ':
            continue

    except KeyError:
        print("Sorry, you entered the incorrect city name. Please, try again.")

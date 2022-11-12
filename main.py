import requests

s_city = "Moscow,RU"
appid = "cbd0d1884dc108b647ee467ed02e15c3"


def weather_day():
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Город:", s_city)
    print("Погодные условия:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])
    print("Минимальная температура:", data['main']['temp_min'])
    print("Скорость ветра:", data['wind']['speed'])
    print("Видимость:", data['visibility'])


def weather_week():
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Прогноз погоды на неделю:")
    for i in data['list']:
        print("Дата <", i['dt_txt'], "> \r\nТемпература<",
              '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодныеусловия <",
              i['weather'][0]['description'], "> \r\n Скорость ветра<",
              i['wind']['speed'], "> \r\n Видимость<",
              i['visibility'], "> ")
        print("_________________________+___")


while (True):
    argument = int(input())
    match argument:
        case 1:
            (weather_day())
        case 2:
            print(weather_week())
        case 3:
            print("Good bey")
            break

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
    A = data['list']
    sum_t = 0
    col_t = 0
    ut_t = str()
    dn_t = str()
    ve_t = str()
    A.append("end")
    for i in range(0, len(A)):
        if A[i + 1] != "end":
            if A[i]['dt_txt'][8:10] == A[i + 1]['dt_txt'][8:10]:
                match int(A[i]['dt_txt'][11:13]):
                    case 6:
                        ut_t = (A[i]['main']['temp'])
                    case 12:
                        dn_t = (A[i]['main']['temp'])
                    case 18:
                        ve_t = (A[i]['main']['temp'])
                sum_t += int(A[i]['main']['temp'])
                col_t += 1
            elif (col_t != 0):
                print("Дата <", A[i]['dt_txt'][:10], "> \r\nТемпература Утром<",
                      (ut_t), "> \r\nТемпература Днём<",
                      (dn_t), "> \r\nТемпература Вечером<",
                      (ve_t), "> \r\nТемпература Средняя<",
                      (sum_t // col_t), ">")
                print("____________________________")
                sum_t = 0
                col_t = 0
        else:
            match int(A[i]['dt_txt'][11:13]):
                case 6:
                    ut_t = (A[i]['main']['temp'])
                case 12:
                    dn_t = (A[i]['main']['temp'])
                case 18:
                    ve_t = (A[i]['main']['temp'])
            sum_t += int(A[i]['main']['temp'])
            col_t += 1
            print("Дата <",A[i]['dt_txt'][:10],"> \r\nТемпература Утром <",
                (ut_t),"> \r\nТемпература Днём<",
                (dn_t),"> \r\nТемпература Вечером<",
                (ve_t),"> \r\nТемпература Средняя<",
                (sum_t // col_t),">")
            print("____________________________")
            break


while (True):
    print("Введите цифру от 1-3 \n"
          "1-Прогноз погоды в Москве на день \n"
          "2-Прогноз погоды в Москве на неделю \n"
          "3-Выход")
    argument = int(input())
    match argument:
        case 1:
            weather_day()
        case 2:
            weather_week()
        case 3:
            print("Good bey")
            break


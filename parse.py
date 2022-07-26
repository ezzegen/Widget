from requests import get
from bs4 import BeautifulSoup


def date(url_date):
    r_date = get(url_date)
    s_date = BeautifulSoup(r_date.text, 'html.parser')
    find_date = s_date.find_all('p', class_="daymonthnow")
    clear_date = [c.text for c in find_date]
    return clear_date[0]


today = date('https://calendaronline.ru/den-segodnya/')


def weather_td(url_w):
    r_weather = get(url_w)
    s_weather = BeautifulSoup(r_weather.text, 'html.parser')
    find_weather = s_weather.find_all('span', class_='dw-into')
    clear_weather = [c.text for c in find_weather][0].split('погода')[1].split('Подробнее')[0]
    change_weather = clear_weather.replace('°C', 'град')
    weather_lst = []
    for i in change_weather.split():
        if i == i.capitalize() and i.isalpha():
            i = '\n' + i
            weather_lst.append(i)
        else:
            weather_lst.append(i)
    return ' '.join(weather_lst)


weather = weather_td('https://world-weather.ru/pogoda/russia/samara/')

if __name__ == '__main__':
    print(date('https://calendaronline.ru/den-segodnya/'))
    print(weather_td('https://world-weather.ru/pogoda/russia/samara/'))

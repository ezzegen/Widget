from requests import get
from bs4 import BeautifulSoup

response_time = get('https://calendaronline.ru/den-segodnya/')
soup_time = BeautifulSoup(response_time.text, 'html.parser')
content_time = soup_time.text
today = [i for i in content_time.split('\n') if i.find('года') != -1][2]

response_weather = get('https://world-weather.ru/pogoda/russia/samara/')
soup_weather = BeautifulSoup(response_weather.text, 'html.parser')
content_weather = soup_weather.text
weather_lst = [i for i in content_weather.split('погода')][1].split('Подробнее')[0]
weather2_lst = []
for i in weather_lst.split():
    if i == i.capitalize() and i.isalpha():
        i = '\n' + i
        weather2_lst.append(i)
    else:
        weather2_lst.append(i)

weather = ' '.join(weather2_lst)

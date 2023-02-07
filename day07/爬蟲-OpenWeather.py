# 天氣資料查詢
# 網路位置: https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}
import json
import requests

city_name = 'taoyuan'
key = 'fcc57465b76d35357c84e4e30fe2431a'
url = 'https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}'.format(city_name, key)
print(url)

data = json.loads(requests.get(url).text)
print(data)
weather_main = data['weather'][0]['main']
weather_description = data['weather'][0]['description']
weather_temp = data['main']['temp'] - 273.15
weather_feels_like = data['main']['feels_like'] - 273.15
weather_humidity = data['main']['humidity']
weather_wind_speed = data['wind']['speed']
weather_clouds = data['clouds']['all']

weather = {}
weather.setdefault('天氣狀況', weather_main)
weather.setdefault('天氣說明', weather_description)
weather.setdefault('現在氣溫', '{:.2f}°C'.format(weather_temp))
weather.setdefault('體感氣溫', '{:.2f}°C'.format(weather_feels_like))
weather.setdefault('現在濕度', '{}%'.format(weather_humidity))
weather.setdefault('現在風速', weather_wind_speed)
weather.setdefault('雲層覆蓋', weather_clouds)
print(weather)

for key in weather.keys():
    # print(key, weather[key])
    print('{}: {}'.format(key, weather[key]))









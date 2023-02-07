# 天氣資料查詢
# 網路位置: https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}
import json
import requests

city_name = 'taoyuan'
key = 'fcc57465b76d35357c84e4e30fe2431a'
url = 'https://api.openweathermap.org/data/2.5/weather?q={},tw&appid={}'.format(city_name, key)
print(url)

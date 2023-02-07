# 資料來源: 行政院農委會
# 資料網址: https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx
import json
import requests


def get_json_str(url):  # 透過指定 url 將 json 字串資料下載下來
    json_str = requests.get(url).text
    return json_str


if __name__ == '__main__':
    url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
    json_str = get_json_str(url);
    print(json_str)


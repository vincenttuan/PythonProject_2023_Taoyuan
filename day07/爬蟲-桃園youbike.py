# 資料來源: 桃園市政府提供
# 網路位置: https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json&limit=5000
# 注意網址後面的 limit=5000 表示最多可以抓 5000 筆資料
import json
import requests


def get_json_str(url):
    json_str = requests.get(url).text
    return json_str


if __name__ == '__main__':
    url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json&limit=5000'
    data_list = json.loads(get_json_str(url))
    # print(data_list)
    records = data_list['result']['records']
    print('資料總筆數:', len(records))
    # print('資料內容:', records)
    # sna = 站名, tot = 總量, sbi = 可借, bemp = 可還, lat = 緯度, lng = 經度
    youbikes = []
    for data in records:
        youbike = {}
        youbike.setdefault('站名', data['sna'])
        youbike.setdefault('總量', int(data['tot']))
        youbike.setdefault('可借', int(data['sbi']))
        youbike.setdefault('可還', int(data['bemp']))
        youbike.setdefault('緯度', float(data['lat']))
        youbike.setdefault('經度', float(data['lng']))
        youbikes.append(youbike)

    print(youbikes)
    # 分析查詢
    # 找出可借數量 > 30 可還數量 > 30 的站台
    result = []
    keyword = input('請輸入站名關鍵字: ')
    for youbike in youbikes:
        #if youbike['可借'] > 30 and youbike['可還'] > 30:
        if keyword in youbike['站名']:
            result.append(youbike)

    # 印出結果
    for i, data in enumerate(result):
        print(i+1, data)

    if len(result) == 0:
        print('查無資料')




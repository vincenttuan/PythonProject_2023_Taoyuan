# 資料來源: 行政院農委會
# 資料網址: https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx
import json
import requests


def get_json_str(url):  # 透過指定 url 將 json 字串資料下載下來
    json_str = requests.get(url).text
    return json_str


if __name__ == '__main__':
    # 1. 原始資料取得
    url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
    json_str = get_json_str(url)
    # print(json_str)
    # 2. 資料傳換成可整理/分析結構
    # 因為 json 字串無法直接分析, 必須透過 json.loads() 轉成數組資料結構才可以分析
    data_list = json.loads(json_str)
    print('資料筆數:', len(data_list))
    print('資料型態:', type(data_list))
    print('資料內容:', data_list)
    # 3. 取得有用的資料欄位
    bad_foods = []
    for data in data_list:
        food = {}
        food.setdefault('不合格時間', data['Title'])
        food.setdefault('品名', data['品名'])
        food.setdefault('不合格原因', data['不合格原因'])
        bad_foods.append(food)
    print(bad_foods)
    # 4. 分析資料
    print('分析資料:')
    result = []  # 用來存放分析結果
    keyword = input('請輸入關鍵字: ')
    for food in bad_foods:
        if keyword in food['品名']:  # 資料比對
            result.append(food)  # 找到資料放入分析結果中
    # 5. 分析結果
    print('分析結果:')
    print('筆數:', len(result))
    print('資料:')
    for i, data in enumerate(result):
        print('{}. 品名: {} 不合格原因: {}'.format(i+1, data['品名'], data['不合格原因']))
    # 6. 保存分析的結果
    if len(result) > 0:
        file = open('result.txt', 'w', encoding='UTF-8')
        for data in result:
            file.write(str(data))  # 寫入資料
            file.write('\n')   # 換行
    else:
        print('查無資料')




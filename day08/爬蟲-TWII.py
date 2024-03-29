# 資料來源: 台灣證券交易所
# 資料位置: https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date={}&selectType=ALL
# 資料格式: 證券代號 證券名稱 殖利率(%) 股利年度 本益比 股價淨值比 財報年/季
import requests
import datetime

def line_notify(dict):
    url = 'https://notify-api.line.me/api/notify'
    token = 'XzuR3y49pyfnXAyahTapEkgawe3Hslhr5zeveJfPWTS'
    headers = {
        "Authorization": "Bearer " + token
    }
    # 輸入要傳送的內容
    msg = '買進 {} {}'.format(dict['證券代號'], dict['證券名稱'])
    payload = {
        "message": msg
    }
    # 傳送到 LineNotify
    resp = requests.post(url, headers=headers, params=payload)
    print(resp)  # 若看到 200 送成功


if __name__ == '__main__':
    date = datetime.datetime(2023, 2, 7)  # 得到日期物件
    print(date)
    date_str = date.strftime('%Y%m%d')  # 將日期物件轉字串
    print(date_str)
    url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date={}&selectType=ALL'.format(date_str)
    print(url)
    data = requests.get(url).text
    # 移除雙引號
    data = data.replace('"', '')
    # 將 - 變成 -1
    data = data.replace('-', '-1')
    # 發現若以 split(',') 來切割每一筆紀錄
    # 有用的紀錄列會等於 8
    twii = []  # 將有用的資料放入此數組中
    for row in data.split('\r\n'):
        row = row.split(',')
        if len(row) == 8:
            # 證券代號 證券名稱 殖利率 股利年度 本益比 股價淨值比 財報
            try:
                dict = {}
                dict.setdefault('證券代號', row[0])
                dict.setdefault('證券名稱', row[1])
                dict.setdefault('殖利率', float(row[2]))
                dict.setdefault('股利年度', row[3])
                dict.setdefault('本益比', float(row[4]))
                dict.setdefault('股價淨值比', float(row[5]))
                dict.setdefault('財報', row[6])
                twii.append(dict)
            except ValueError:
                pass
    # print(twii)
    # 若要買一檔股票, 以下是教課書給的意見參數
    # 本益比 <= 12
    # 殖利率 >= 7
    # 股價淨值比 <= 1
    for t in twii:
        # 除去有負值的資料
        if 0 < t['本益比'] <= 12 and t['殖利率'] >= 7 and 0 < t['股價淨值比'] <= 1:
            print(t)
            line_notify(t)

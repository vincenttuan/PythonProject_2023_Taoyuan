# LineNotify
# 通知的位置: https://notify-api.line.me/api/notify
# token = XzuR3y49pyfnXAyahTapEkgawe3Hslhr5zeveJfPWTS
import requests

if __name__ == '__main__':
    url = 'https://notify-api.line.me/api/notify'
    token = 'XzuR3y49pyfnXAyahTapEkgawe3Hslhr5zeveJfPWTS'
    headers = {
        "Authorization": "Bearer " + token
    }
    # 設定網路圖片位置訊息
    msg = 'Car'
    file = {'imageFile': open('car.jpg', 'rb')}
    payload = {
        "message": msg
    }
    # 傳送到 LineNotify
    resp = requests.post(url, headers=headers, params=payload, files=file)
    print(resp)  # 若看到 200 送成功



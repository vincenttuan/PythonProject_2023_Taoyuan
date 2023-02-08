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
    # 輸入要傳送的內容
    msg = input('請輸入文字訊息: ')
    payload = {
        "message": msg
    }
    # 傳送到 LineNotify
    resp = requests.post(url, headers=headers, params=payload)
    print(resp)  # 若看到 200 送成功



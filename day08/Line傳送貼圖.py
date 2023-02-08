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
    # 設定要傳送的文字
    msg = ' '
    # 設定要傳送的貼圖
    stickerPackageId = 6362
    stickerId = 11087924
    payload = {
        "message": msg,
        "stickerPackageId": stickerPackageId,
        "stickerId": stickerId
    }
    # 傳送到 LineNotify
    resp = requests.post(url, headers=headers, params=payload)
    print(resp)  # 若看到 200 送成功

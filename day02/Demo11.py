# if - else 練習
# 使用者輸入一個數字, 系統可以判斷奇/偶數
try:
    n = int(input('輸入一個數:'))
    if n % 2 == 0:
        print(n, '是偶數')
    else:
        print(n, '是奇數')
except:
    print('資料輸入錯誤')


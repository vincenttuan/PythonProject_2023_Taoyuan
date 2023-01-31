import math
# 基本輸入 input() 直接傳型
try:
    h = float(input('請輸入身高: '))
    w = float(input('請輸入體重: '))
    # case 1
    bmi = w / (h / 100) ** 2
    # case 2 利用 math.pow(x, n) 作用 x 的 n 次方
    bmi = w / math.pow(h / 100, 2)
    print('BMI = %.2f' % bmi)
except:
    print('身高/體重必須是數字資料')

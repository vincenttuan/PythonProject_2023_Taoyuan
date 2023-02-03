# 有三組(h, w)資料 170, 50 ; 180, 70 ; 160, 60
# 請試做一個 def calcBmi 方法
# calcBmi 方法可以輸入 2 個參數
# 可以印出 bmi 值 與 bmi 是否正常 (18<bmi<=23 正常範圍)

def getBmi(h, w):
    bmi = w / (h/100)**2
    return bmi

def checkBmi(bmi):
    result = '正常'  # 假設是正常
    if bmi > 23:
        result = '過胖'
    elif bmi <= 18:
        result = '過輕'
    return result

def calcBmi(h, w):
    # 1. 計算 bmi
    bmi = getBmi(h, w)
    # 2. 驗證 bmi 是否正常
    result = checkBmi(bmi)
    # 3. 印出所需結果
    print('BMI: {0:.2f} {1}'.format(bmi, result))


if __name__ == '__main__':
    calcBmi(170, 50)
    calcBmi(180, 70)
    calcBmi(160, 60)

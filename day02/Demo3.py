# 基本輸入 input()
h = input('請輸入身高: ')
w = input('請輸入體重: ')
# 查看所得到的變數內容與型態
print(h, type(h))
print(w, type(w))
# 改變 h, w 的資料型別 str -> float
h = float(h)
w = float(w)
print(h, type(h))
print(w, type(w))
# 計算 bmi
bmi = w / (h/100)**2
print('BMI = %.1f' % bmi)

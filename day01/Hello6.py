# 變數的應用
# 計算 BMI 值
# 公式: 體重 / (身高(公尺)的平方)
w = 60  # 體重(kg)
h = 170  # 身高(cm)
# 請計算出 BMI 的值
h = h/100  # 先將 h/100 身高(m)
bmi = w / (h*h)
print('BMI =', bmi)

bmi = w / h**2  # ** 次方
print('BMI =', bmi)





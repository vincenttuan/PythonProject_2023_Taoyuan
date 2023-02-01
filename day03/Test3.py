# 請問 BMI = ?
data = "身高=170,體重=60.5"
data = data.split(",")
print(data)
# ---------------------------
height = data[0]
height = height.split("=")
height = height[1]
print(height, type(height))
# ---------------------------
weight = data[1]
weight = weight.split("=")
weight = weight[1]
print(weight, type(weight))
# ---------------------------
h = float(height)
w = float(weight)
bmi = w / (h/100)**2
print('%.2f' % bmi)

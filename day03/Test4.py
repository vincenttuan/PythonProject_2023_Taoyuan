# 求總分與平均
data = '國文=100,數學=90,英文:70'
data = data.split(",")
print(data)
# ------------------------------------
chinese = int(data[0].split("=")[1])
print(chinese, type(chinese))
math = int(data[1].split("=")[1])
print(math, type(math))
english = int(data[2].split(":")[1])
print(english, type(english))
# ------------------------------------
total = chinese + math + english
avg = total / 3
print(total, avg)
print("總分: {0} 平均: {1:.1f}".format(total, avg))

import math
# math 的應用
# math.pow(x, n) -> x 的 n 次方
# math.sqrt(x) -> 開根號
a = math.pow(2, 3)
b = math.sqrt(9)
print(a, b)

# 題目: 二點間的距離
# A點(10, 20), B點(-50, 30)
# 求AB二點間的距離 = ?
x1, y1 = 10, 20  # A點
x2, y2 = -50, 30  # B點
dx = math.pow(x1-x2, 2)
dy = math.pow(y1-y2, 2)
d = math.sqrt(dx + dy)
print('距離: %.1f' % d)


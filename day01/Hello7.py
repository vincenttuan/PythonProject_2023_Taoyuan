# 變數應用
# 已知半徑 r = 9
# 求圓面積 = ? (印出的內容到小數點一位)
import math

r = input('請輸入半徑: ')
print(r, type(r))
r = int(r)  # 將 r 轉為 int 型態
print(r, type(r))
#pi = 3.1415236
pi = math.pi  # 透過 python 內建的數學函式來取得圓周率
print(pi)
area = r**2 * pi
print('圓面積 = %.1f' % area)


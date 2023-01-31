# python 保留字
import keyword
print(keyword.kwlist)

# 變數的覆值
a = b = c = 100
age, name = 18, "John"

# 浮點數
pi = 3.14
value = 3.14e2  # 科學記號 e2 -> 表示10的2次方
print(pi, value)
print(type(pi), type(value))

# 綜合練習
a, b, c, d = 10, 20.5, True, 'Mary'
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))

# 刪除變數
del a  # 將 a 變數刪除
print(a)  # 此行執行時會發生錯誤

# 轉型(變態 = 改變資料的型別)
# int -> str
# str -> float
chinese = '100'
math = 90
print(chinese, type(chinese))
print(math, type(math))

# 需先將 chinese 轉型
chinese = int(chinese)
total = chinese + math
print(total)


# 數組 list
a = [1, 3, 5, 7, 5]  # list: 內容可以重複, 可以變更
print(a)
a[0] = 2  # 變更元素0的內容
print(a)
a.append(9)  # 增加元素
print(a)
a.remove(5)  # 移除元素
print(a)
a.reverse()  # 列表反轉
print(a)
a.sort()  # 列表元素排序(小->大)
print(a)
print(max(a))  # 取元素最大值
print(min(a))  # 取元素最小值
a = tuple(a)  # 將列表 a 設定為唯讀
print(a)


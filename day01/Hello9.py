# 今有雞、兔同籠，上有三十五頭，下九十四足。問雞、兔各幾何？
'''
算式:
假設都是雞那會有幾隻腳
35 * 2 = 70
94 - (35 * 2) = 24/(4-2) = 12
35 - 12 = 23
'''
total = 35
feet = 70
print('今有雞、兔同籠，上有 %d 頭，下 %d 足。問雞、兔各幾何？' % (total, feet))
rabbit = (feet - total*2) / (4-2)
chicken = total - rabbit
print('雞 = %d, 兔 = %d' % (chicken, rabbit))



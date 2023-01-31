# print + format
cash = 123456789.54321
# 加上千分號到小數點2位 -> 123,456,789.54
print("%.2f" % cash)
print("%s" % format(cash, ","))
print("%s" % format(float("%.2f" % cash), ","))
#-----------------------------------------------
language = 'Python'
version = 3210.11
print('程式語言: {0}\n版本編號: {1:,}'.format(language, version))

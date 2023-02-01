data = '小明本薪$65000,今年公司發放6個月,試問小明年終'
print(data)
print(data[5:10])
print(data.find('$') + 1)
print(data.find(','))
print(data[data.find('$') + 1:data.find(',')])
print(data[data.find('發放') + 2:data.find('個月')])
# ------------------------------------------------------
salary = int(data[data.find('$') + 1:data.find(',')])
month = int(data[data.find('發放') + 2:data.find('個月')])
total = salary * month
print("年終 ${0:,}".format(total))
print("年終 ${:,}".format(total))

file = open('salary.txt', 'r', encoding='UTF-8')
# 讀取整個檔案到數組(串列, 陣列)
rows = file.readlines()
print(rows)
# 將每一筆資料放到 dict 的結構中
# Ex: {'name': 'John', 'salary': 45000}
# 目的:
# [
#   {'name': 'John', 'salary': 45000},
#   {'name': 'Mary', 'salary': 55000},
#   {'name': 'Jack', 'salary': 65000},
#   {'name': 'Mole', 'salary': 75000},
#   {'name': 'Acer', 'salary': 85000}
# ]
# 逐一印出每一筆員工姓名與薪資
# 進行資料處理 ...
employees = []
for row in rows:
    #print(row)
    data = row.split()
    #print(data)
    dict = {}
    dict.setdefault('name', data[0])
    dict.setdefault('salary', int(data[1]))
    #print(dict)
    employees.append(dict)

print(employees)

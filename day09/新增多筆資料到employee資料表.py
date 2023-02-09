import sqlite3
# 新增多筆資料到 employee 資料表中
sql = '''
    insert into employee(employee_name, employee_salary)
    values(?, ?) 
'''
sql = sql.strip()
records = [
    ('Mary', 55000), ('Bob', 35000), ('Helen', 42000), ('Alen', 85000), ('Jo', 120000)
]
print(sql)
print(records)

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor = cursor.executemany(sql, records)
print('新增資料筆數: {}'.format(cursor.rowcount))
conn.commit()  # 提交任務 (重要!!!)
conn.close()

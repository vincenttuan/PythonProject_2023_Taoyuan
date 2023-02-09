import sqlite3
# 新增一筆資料到 employee 資料表
sql = '''
    insert into employee(employee_name, employee_salary)
    values('{0}', {1}) 
'''
sql = sql.strip()
sql = sql.format('John', 45000)
print(sql)

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor = cursor.execute(sql)
print('新增資料筆數: {}'.format(cursor.rowcount))
print('此次新增的 id 值: {}'.format(cursor.lastrowid))
conn.commit()  # 提交任務 (重要!!!)
conn.close()





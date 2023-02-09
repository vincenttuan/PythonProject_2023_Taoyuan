import sqlite3
# 修改 employee 資料表
sql = 'update employee set employee_name = ?, employee_salary = ? where id = ?'

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
employee_name = 'Happy'
employee_salary = 66000
id = 1
params = [employee_name, employee_salary, id]
cursor = cursor.execute(sql, params)
print('修改筆數: {}'.format(cursor.rowcount))
conn.commit()
conn.close()

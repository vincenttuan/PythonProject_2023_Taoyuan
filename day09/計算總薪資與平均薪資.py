import sqlite3
sql = 'select SUM(employee_salary), AVG(employee_salary) from employee'
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor = cursor.execute(sql)
data = cursor.fetchone()
print(data)
print('總薪資:${:,} 平均薪資:${:,}'.format(data[0], data[1]))
conn.close()

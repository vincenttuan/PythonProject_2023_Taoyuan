import sqlite3
# 建立 employee 資料表
# 欄位: id, employee_name, employee_salary, create_time
sql = '''
    create table if not exists employee(
        id integer not null primary key autoincrement,
        employee_name text not null,
        employee_salary integer,
        create_time timestamp default current_timestamp
    )
'''
sql = sql.strip()  # 去除字串左右空白
print(sql)
# 1. 開啟資料庫連線
conn = sqlite3.connect('demo.db')
# 2. 得到 cursor 才可以操作資料庫
cursor = conn.cursor()
# 3. 執行 sql 指令
cursor.execute(sql)
# 4. 任務提交
conn.commit()
# 5. 關閉連線
conn.close()
print('資料表建立完成')




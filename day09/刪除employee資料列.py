import sqlite3
# 刪除 employee 資料列
sql = 'delete from employee where id = ?'
conn = sqlite3.connect(sql)
cursor = conn.cursor()
delete_id = 2  # 要刪除的 id
param = [delete_id]
cursor = cursor.execute(sql, param)
print('刪除筆數: {}'.format(cursor.rowcount))



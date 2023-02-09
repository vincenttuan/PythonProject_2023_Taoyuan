# 資料庫就是囤放多張資料表
# 每張資料表可以放置多筆紀錄
# 每一筆紀錄可以存放多筆欄位
# 欄位內就是資料
# 建立一個 demo.db 的資料庫
import sqlite3

conn = sqlite3.connect('demo.db')  # 建立資料庫連線
print('建立資料庫成功', conn)
conn.close()  # 將資料庫連線關閉


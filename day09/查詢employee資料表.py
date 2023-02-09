import sqlite3
# 查詢 employee 資料表
# 全部查詢


def find_all():
    sql = 'select id, employee_name, employee_salary, create_time from employee'
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor = cursor.execute(sql)
    rows = cursor.fetchall()  # 得到所有回傳紀錄
    return rows


if __name__ == '__main__':
    employees = find_all()
    # 將資料印出
    print('%2s %-6s %8s %-24s' % ('ID', 'Name', 'Salary', 'Time'))
    print('---------------------------------------')
    for emp in employees:
        print('%2d %-6s %8s %-24s' % (emp[0], emp[1], '{:,}'.format(emp[2]), emp[3]))
    print('---------------------------------------')



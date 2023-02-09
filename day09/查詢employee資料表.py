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


def find_one(id):
    sql = 'select id, employee_name, employee_salary, create_time from employee where id = ?'
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor = cursor.execute(sql, [id])
    row = cursor.fetchone()
    return row


def print_employee(employees):
    # 將資料印出
    print('%2s %-6s %8s %-24s' % ('ID', 'Name', 'Salary', 'Time'))
    print('---------------------------------------')
    if employees is None or employees[0] is None:
        print(' 查無資料')
    else:
        for emp in employees:
            print('%2d %-6s %8s %-24s' % (emp[0], emp[1], '{:,}'.format(emp[2]), emp[3]))
    print('---------------------------------------')


if __name__ == '__main__':
    # 多筆
    employees = find_all()
    # 將資料印出
    print_employee(employees)

    # 單筆
    emp = find_one(1)
    print_employee([emp])

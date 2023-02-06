from day06.ReadFile import get_employees_from_file
# 分析資料
# 從 salary.txt 中得到所有員工薪資的總和
if __name__ == '__main__':
    employees = get_employees_from_file('salary.txt')
    salary = [emp['salary'] for emp in employees]
    print(salary)
    print('薪資總和: {:,}'.format(sum(salary)))


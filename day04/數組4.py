# 數組 dict (字典格式)
emp1 = {'name': 'John', 'salary': 50000}
print(emp1)
print(emp1['name'], type(emp1['name']))
print(emp1['salary'], type(emp1['salary']))
emp2 = {'name': 'Mary', 'salary': 60000}
emp3 = {'name': 'Bobo', 'salary': 70000}
# 將 emp1, emp2, emp3 放到 list 數組中
employees = [emp1, emp2, emp3]
print(employees)
# 計算總薪資
total = 0  # 累計薪資
for emp in employees:
    print(emp)
    total = total + emp['salary']

print('{:,}'.format(total))
# 平均薪資 = ?
print('{:,}'.format(total/len(employees)))
# 最高薪資 = ?
high_salary = 0  # 假設最高薪資是 0
for emp in employees:
    if emp['salary'] > high_salary:
        high_salary = emp['salary']

print(high_salary)
# 最低薪資 = ?
low_salary = high_salary
for emp in employees:
    if emp['salary'] < low_salary:
        low_salary = emp['salary']

print(low_salary)

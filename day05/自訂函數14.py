emp1 = {'name': 'John', 'salary': 50000, 'program': ['Java', 'Python']}
emp2 = {'name': 'Mary', 'salary': 70000, 'program': ['C++', 'Java']}
emp3 = {'name': 'Alen', 'salary': 80000, 'program': ['VB', 'Python']}
emp4 = {'name': 'Cube', 'salary': 60000, 'program': ['C#']}
employees = [emp1, emp2, emp3, emp4]
print(employees)
# 請印出會 Python 的員工姓名 ?
names = []
for emp in employees:
    # print(emp['program'], emp['program'].count('Python'))
    if emp['program'].count('Python') > 0:
        names.append(emp['name'])

print(names)


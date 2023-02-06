import statistics as stat
from day06.ReadFile import get_employees_from_file
# 分析資料
# 從 salary.txt 中得到所有員工薪資的總和
if __name__ == '__main__':
    employees = get_employees_from_file('salary.txt')
    salary = [emp['salary'] for emp in employees]
    print(salary)
    print('薪資總和: {:,}'.format(sum(salary)))
    print('薪資最低: {:,}'.format(min(salary)))
    print('薪資最高: {:,}'.format(max(salary)))
    # 透過統計函式來計算
    print('薪資平均: {:,}'.format(stat.mean(salary)))
    print('薪資平均: {:,}'.format(stat.fmean(salary)))  # fmean() 浮點數快速平均
    print('薪資中位數: {:,}'.format(stat.median(salary)))
    print('薪資標準差: {:,.2f}'.format(stat.stdev(salary)))
    print('薪資變異係數: {:,.2f}'.format(stat.stdev(salary)/stat.mean(salary)))

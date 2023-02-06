import matplotlib.pyplot as plt
import statistics as stat
from day06.ReadFile import get_employees_from_file
if __name__ == '__main__':
    employees_salary = get_employees_from_file('salary.txt')
    employees_age = get_employees_from_file('age.txt', col_name2='age')
    print(employees_salary)
    print(employees_age)
    # 比較 salary 與 age 哪一個分散程度大(集中度小)?
    # 透過變異係數 CV 來判定
    # CV 越大表示分散程度越大(集中度小)反之CV 越小表示分散程度越小(集中度大)
    # CV(變異係數) 與 SD(標準差)的不同是
    # CV 用來比較不同單位的差異, SD 用來比較同單位的差異
    # 計算 salary 的 CV
    salary = [emp['salary'] for emp in employees_salary]
    salary_cv = stat.stdev(salary) / stat.mean(salary)
    # 計算 age 的 CV
    age = [emp['age'] for emp in employees_age]
    age_cv = stat.stdev(age) / stat.mean(age)
    print('salary cv: {:.3f} age cv: {:.3f}'.format(salary_cv, age_cv))
    print('{0}的分散程度大'.format('salary' if salary_cv > age_cv else 'age'))

    # 繪圖
    salary = [sal//1000 for sal in salary]
    names = [emp['name'] for emp in employees_salary]
    # print(names)
    # 設定圖表中文字形
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 將字體設定為微軟預設中文字型
    plt.rcParams['axes.unicode_minus'] = False  # 用來正常顯示負號

    plt.plot(names, salary, marker="o", label='薪資(K)')
    plt.plot(names, age, marker="o", label='年齡')
    plt.grid(True)  # 加入格線
    plt.title('員工統計圖表')
    plt.legend()  # 加上圖例
    plt.ylabel('年齡/薪資(K)')
    plt.show()


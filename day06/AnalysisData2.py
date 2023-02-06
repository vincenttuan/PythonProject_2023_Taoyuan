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



# 自訂函數: * 與 **
def print_score(**exam):  # dict
    print(exam)
    print(exam.keys(), type(exam.keys()))  # 得到所有考試科目
    print(exam.values(), type(exam.values()))  # 得到所有考試成績
    print(sum(exam.values()))


if __name__ == '__main__':
    print_score(國文=100, 數學=80, english=70)


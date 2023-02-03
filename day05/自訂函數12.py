# 自訂函數: 函數式參數
def add(x):
    return x + 1


def sub(x):
    return x - 1


def operator(func, x):
    return func(x)


if __name__ == '__main__':
    print(add(10))  # 11
    print(sub(10))  # 9

    x = operator(add, 10)
    print(x)  # 11

    y = operator(sub, 10)
    print(y)  # 9

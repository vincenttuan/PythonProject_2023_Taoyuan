# 自訂涵式: 有回傳值
def div(x, y):
    result = x / y
    return result


def mult(x, y):
    result = x * y
    return result


# 主程式
if __name__ == '__main__':
    res1 = div(10, 2)
    print(res1)
    res2 = mult(10, 2)
    print(res2)

# 自訂涵式: 有多筆回傳值
# 同時計算並回傳 x 與 y 的乘除結果
def divAndMulti(x, y):
    result1 = x / y
    result2 = x * y
    return result1, result2


if __name__ == '__main__':
    res1, res2 = divAndMulti(10, 2)
    print(res1)
    print(res2)



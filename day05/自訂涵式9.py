# 自訂函數: * 與 **
def get_total(*num):  # tuple
    print(type(num), num)
    return sum(num)


if __name__ == '__main__':
    total1 = get_total(10, 20, 30)
    total2 = get_total(10, 20)
    total3 = get_total()
    total4 = get_total(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    print(total1, total2, total3, total4)


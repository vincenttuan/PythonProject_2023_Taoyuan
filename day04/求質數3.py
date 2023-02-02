# 求小於 10000 的最大值數
for x in range(9999, 1, -1):
    is_prime = True
    for i in range(2, x//2+1):
        if x % i == 0:
            is_prime = False
            break  # 跳離內層迴圈
    if is_prime:
        print(x)
        break  # 跳離外層迴圈



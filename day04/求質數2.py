# 請印出 2~100 的質數
for x in range(2, 101):
    is_prime = True  # 起初假設 x 是質數
    for i in range(2, x//2 + 1):
        if x % i == 0:
            is_prime = False  # x 不是質數
            break
    if is_prime:  # 若 x 是質數
        print(x)



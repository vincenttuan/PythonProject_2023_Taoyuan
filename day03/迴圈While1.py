# while 迴圈
import random as r
while True:
    n = r.randint(1, 99)
    if n % 2 == 0:
        continue
    print(n)
    if n == 99:
        break  # 跳離迴圈

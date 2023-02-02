import random as r
# for loop 步進迴圈
for i in range(1, 5):  # 1, 2, 3, 4
    print(i)
# -----------------------------------
for i in range(1, 5):
    print('java')
# -----------------------------------
for i in range(1, 5):
    print(i, 'java')
# -----------------------------------
# 電腦選4個號碼
for i in range(0, 4):
    print(r.randint(1, 9), end=' ')
print()
# -----------------------------------
for i in range(1, 10, 3):
    print(i)
# -----------------------------------
# for 迴圈與數組的關係
for score in [100, 90, 80, 70, 60]:
    print(score)
# -----------------------------------
for i, score in enumerate([100, 90, 80, 70, 60]):
    print(i, score)

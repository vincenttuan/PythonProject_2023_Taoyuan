import random as r
# 1~9 猜一數字
# 若猜得比答案小 -> 顯示猜小了
# 若猜得比答案大 -> 顯示猜大了
ans = r.randint(1, 9)
while True:
    guess = int(input('1~9 請猜一個數字:'))
    if guess > ans:
        print('猜大了')
    elif guess < ans:
        print('猜小了')
    else:
        print('答案: {} 玩家贏了'.format(ans))
        break

print('遊戲結束')

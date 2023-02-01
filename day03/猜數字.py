import random as r
# 1~9 猜一數字
# 若猜得比答案小 -> 顯示猜小了
# 若猜得比答案大 -> 顯示猜大了
ans = r.randint(1, 9)
while True:
    # 玩家猜
    guess = input('玩家 1~9 請猜一個數字: ')
    # 判斷是否輸入的都是數字
    if not guess.isdigit():
        print('請輸入數字')
        continue
    # 資料轉型 str -> int
    guess = int(guess)
    # 先過濾玩家所猜的數字是不是在合理範圍內
    if guess < 1 or guess > 9:
        print('數字不在 1~9 範圍內, 請重猜!')
        continue
    # 比對答案
    if guess > ans:
        print('猜大了')
    elif guess < ans:
        print('猜小了')
    else:
        print('答案: {} 玩家贏了'.format(ans))
        break

print('遊戲結束')

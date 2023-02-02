import random as r
# 數組 set
lotto = set()
lotto.add(10)
lotto.add(20)
lotto.add(30)
lotto.add(35)
lotto.add(15)
lotto.add(15)
print(lotto)
print(len(lotto))
# 樂透 539, 1~39 取出 5 個不會重複的數字
# 請透過 random 來模擬電腦選號

lotto = set()
while len(lotto) < 5:
    n = r.randint(1, 39)
    lotto.add(n)
    print(n, len(lotto))

print(lotto)


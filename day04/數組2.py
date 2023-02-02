# 撲克牌
import random as r
poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
print(poker)
print(len(poker))
# 洗牌 (換位置)
poker[0], poker[1] = poker[1], poker[0]
print(poker)

for i in range(0, 100):
    first = r.randint(0, 51)
    second = r.randint(0, 51)
    poker[first], poker[second] = poker[second], poker[first]

print(poker)

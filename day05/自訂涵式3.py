# 自訂涵式
# 如何使用自己在其他.py寫的自訂涵式
from day05.自訂涵式1 import hello
from day05.自訂涵式2 import add

if __name__ == '__main__':
    hello()
    hello()
    add(10, 20)
    add(30, 40)

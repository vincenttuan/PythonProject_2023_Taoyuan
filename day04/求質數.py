# 請判斷 9, 7 是否是質數 ?
is_prime = True
num = 9
# num = 7
for n in range(2, num//2 + 1):
    print(num, '%', n, '==', num % n == 0)
    if num % n == 0:
        is_prime = False
        break

print('{} 是否是質數: {}'.format(num, is_prime))



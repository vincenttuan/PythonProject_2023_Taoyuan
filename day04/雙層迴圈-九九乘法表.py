for x in range(1, 10):
    for y in range(1, 10):
        print('%d*%d=%-2d' % (x, y, (x * y)), end=' ')
    print()  # 換行

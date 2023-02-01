# 字串分析
words = "she sell sea shell on the sea shore"
print(words, len(words))
print(words[2:10])
print('有幾個 s:', words.count('s'))
print('sea 的位置:', words.find('sea'))
print('she 的位置:', words.find('she'))
print('sky 的位置:', words.find('sky'))
# 是否有 on ?
if words.find('on') != -1:
    print('有 on, 位置在:', words.find('on'))
else:
    print('無 on')
# --------------------------------------------------
print('有 on' if words.find('on') != -1 else '無 on')
result = '有 on' if words.find('on') != -1 else '無 on'
print(result)


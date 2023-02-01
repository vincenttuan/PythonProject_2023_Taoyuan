data = "一杯咖啡55元買一送一, 小明買5 杯總共花多少錢"
price = data[data.find('咖啡')+2:data.find('元')]
cup = data[data.find('小明買')+3:data.find('杯總')].strip()  # strip() 去除空白
print(price, cup)
price = int(price)
cup = int(cup)
print(price, cup)
amount = cup // 2 + (0 if cup % 2 == 0 else 1)
print(amount * price)
print(price * (cup - cup//2))





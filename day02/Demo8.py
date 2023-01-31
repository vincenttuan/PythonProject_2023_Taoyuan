# 綜合練習
symbol = '2330'  # 股票代號
name = '台積電'  # 股票名稱
price = 510  # 股票目前價格
# ----------------------------------
buy_price = 495  # 每一股的買進股票價格
amount = 3000  # 買進的股票股數
total = buy_price * 3000  # 投資金額
print("%s %s 目前價格:%d 買進價格:%d 買進股數:%d 投資金額:%d" % (symbol, name, price, buy_price, amount, total))
print("投資金額:%d" % total)
print("投資金額:%s" % format(total, ","))  # 利用 format() 加入千分號
print("%s %s 目前價格:%d 買進價格:%d 買進股數:%s 投資金額:%s" %
      (symbol, name, price, buy_price, format(amount, ","), format(total, ",")))


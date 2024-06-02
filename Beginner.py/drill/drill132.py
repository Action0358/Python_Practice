#  コード1-22 データ型変換
x = 3.14
y = int(x)
print(y)
print(type(y)) # int型にしたので、小数点以下が切り捨て

z = str(x)
print(z)
print(z * 2)
print(type(z)) # 文字列なので、「*」で3.14が2回出力される

#  コード1-23 割り勘計算プログラムの修正(未完了)
price = input('料金を入力 >>')
price = int(price)
number = input('人数を入力 >>')
number = int(number)
payment = price / number
print('お支払いは' + str(payment) + '円です') # 原則、文字列同士か数理同士

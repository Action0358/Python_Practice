# コード1-16 変数の現在の値に加減乗除する(複合代入演算子)
age = 24
age += 1 

print(age)

price = 2600
price *= 1.5

print(price)

# 1-17 キーボードから値を入力
name = input("あなたの名前を入力してください >>") # 引数入力
print("おお" + name + "よ、そなたが来るのを待っておったぞ！" )

# 1-18 割り勘計算プログラム
price = input("料金を入力 >>") # 引数入力
number = input("人数を入力 >>") #　引数入力

price = int(price)
number = int(number)

payment = price // number
print("お支払いは" + str(payment) + "円です")

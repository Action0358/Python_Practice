#  コード1-19 変数には異なるデータ型の値を代入できる

x = '松田' # 名前
print(x)

x = 23 # 年齢
print(x)

x = 175.6 # 身長
print(x)

#  コード1-20 格納されている値のデータを調べる
x = 10
print(type(x))

#  割り勘計算プログラムの問題点(input関数で入力した値は、文字列として扱われる)
price = input('料金を入力 >>')
print (type(price))
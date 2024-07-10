#  コード1-24 文字列に変数を埋め込む
name = '松田光太'
age = 23
height = 175.6

print('私の名前は' + name + 'で、年齢は' + str(age) + '歳で、身長は' + str(height) + 'cmです')

#  コード1-25 format関数で文字列に数値を埋め込む
name = '松田光太'
age = 23
height = 175.6

print('私の名前は{}で、年齢は{}歳で、身長は{}cmです'.format(name, age, height))

#  コード1-26   割り勘計算プログラム(完成版)
price = int(input("料金を入力 >>")) # 引数入力
number = int(input('人数を入力 >>')) # 引数入力
payment = int(price / number)

print("お支払いは{}です".format(payment))
# 前の２つの要素を足した数値が次の要素となるnumbersに追加していく（追加する値は1000を超えないものとする）
# numbersにある要素の値 ÷ 1つ前の要素の値を要素とした新しいリストratiosを作成
# ratiosにある各要素の値が小数点第３位まで表示されるように更新する

numbers = [1, 1]
data = sum(numbers)
count = 2

while data <= 1000:
    numbers.append(data)
    data = data + numbers[count - 1]
    count += 1
    
print(numbers)

ratios = list()

for i in range(len(numbers)):
    if i == len(numbers) - 1:
        break
    
    ratios.append(numbers[i + 1] / numbers[i])

print(ratios)

print(['{:.3f}'.format(ratio) for ratio in ratios])




# ループのステップごとの説明
# 初期状態
# numbers = [1, 1]
# data = 2
# count = 2

# while data <= 1000 の条件が真なのでループ開始
# numbers.append(data) により、numbers リストに data を追加
# numbers = [1, 1, 2]
# data = data + numbers[count - 1] で data の新しい値を計算
# count - 1 = 2 - 1 = 1
# numbers[1] は 1 
# data = 2 + 1 = 3
# count += 1 でカウントを増やす
# count = 3

# このステップの後の状態：
# numbers = [1, 1, 2]
# data = 3
# count = 3

# range関数とlen関数(例題)
# >>> x = [0, 2, 4, 6] #リストをXに代入
# >>> for i in range(len(x)): len(x)は要素数4個であり、range(len(x))はlen(x)の要素番号である
#         print(i)
 
# #出力結果
# 0
# 1
# 2
# 3

# print(['{:.3f}'.format(ratio) for ratio in ratios])
# リストの要素を全て小数第3桁までの値にフォーマットし、新たなリストとしている。
# ratioという変数名 は、ratios リスト内の各値を順に指します。(変数名は任意である)
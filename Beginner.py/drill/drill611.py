# コード6-1 append関数やformat関数の呼び出し
tpl = "3人目は{}さん"
names = ["松田", "浅木"]

names.append("工藤")

# names[2]はリストの3番目の要素を指します
message = tpl.format(names[2])
print(message)


# コード6-2 全ての値がデータと関数を持つ
num = 10
print(num.bit_length())


names = ["松田", "浅木"]
names.append("工藤")
print(names)


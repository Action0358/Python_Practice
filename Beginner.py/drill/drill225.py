# コード2-8 リストに要素を追加
members = ["工藤", "松田", "浅木"]
members.append("菅原")
members.append("湊")
members.append("朝香")
print(members)

# コード2-9 リストに要素を削除
members = ["工藤", "松田", "浅木"]
members.remove("松田")
print(members)

# コード2-10 リストに要素を変更
members = ["工藤", "松田", "浅木"]
members[0] = "菅原"
print(members)

# コード2-11 スライスによる範囲指定
a = [10, 20, 30, 40, 50]
print(a[1:3]) # 添え字が1以上3未満の要素
print(a[2:]) # 添え字が2以上の全ての要素
print(a[:3]) # 添え字が3未満のすべての要素

# コード2-12 負の数による指定
a = [10, 20, 30, 40, 50]
print(a[-1]) # 末尾の要素を参照
print(a[-2]) # 末尾から2番目の要素を参照
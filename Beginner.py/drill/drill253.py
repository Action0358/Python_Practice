#　コード2-27 2人の共通点を探す
member_hobbies = {
    "松田" : {"SNS", "麻雀", "自転車"},
    "浅木" : {"麻雀", "食べ歩き", "数学", "数学", "数学"}
}
common_hobbies = member_hobbies["松田"] & member_hobbies["浅木"]
# 2人に共通する趣味一覧を表示する
print(common_hobbies)

# コード２-28 4つの集合演算
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
print(A | B) # 和集合
print(A & B) # 積集合
print(A - B) # 差集合
print(A ^ B) # 対称差
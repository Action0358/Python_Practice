#コード2-24 ディクショナリの中にディクショナリをネスト
matsuda_scores = {"network": 60, "database": 80, "security": 50}
asagi_scores = {"network": 80, "database": 75, "security": 92}
member_scores = {
    "松田": matsuda_scores,
    "浅木": asagi_scores
}

#コード2-25 ディクショナリの中にセットをネスト
member_hobbies = {
    "松田" : {"SNS", "麻雀", "自転車"},
    "浅木" : {"麻雀", "食べ歩き", "数学", "数学", "数学"}
}
#全員の趣味一覧を表示する
print(member_hobbies)
#松田くんの趣味一覧を表示する
print(member_hobbies["松田"])
#浅木さんの趣味一覧を表示する
print(member_hobbies["浅木"])

#コード2-26 2次元リストの例（リストの中にリストを入れた構造）
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

print(c) #リストc全体を参照
print(c[0]) #リストcの0番目（リストa）だけを参照
print(c[1][2]) #リストcの1番目（リストb）の2番目だけを参照
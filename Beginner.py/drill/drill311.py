# 1行が1つの文とならない書き方

# 文の終わりに;を入れると、 １行に複数の文を記述できる
name = "松田"; print(f"僕の名前は{name}です")

# 1行を複数行に分けて記述するには、\を行末に記述する
n = 1 + 2 \
    + 3
print(f"答えは{n}\
改行しても足し算できていますね")
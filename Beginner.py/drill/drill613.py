# コード6-3 文字列のメソッドを活用した血液型占い
userinfo = input("名前と血液型をカンマで区切って１行で入力 >>")

[name, blood] = userinfo.split(",")

blood = blood.upper().strip()

print(f"{name}さんは{blood}型なので大吉です")


# 関数さえオブジェクト
def add(x, y):
    return x + y

type(add)

newadd = add

print(newadd(4, 5))

# コード6-4 リテラルやクラス名関数を用いたオブジェクトの生成
int_value1 = 0
int_value2 = int()
int_value3 = int(9)

list_value1 = []
list_value2 = list()
list_value3 = list(("松田", "浅木"))
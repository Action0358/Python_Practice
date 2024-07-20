# コード6-7 リストオブジェクトのコピーによる不可解な動作
scores1 = [80, 40, 50]
scores2 = [80, 40, 50]

print(f"scores1の先頭要素は{scores1[0]}")
print(f"scores2の先頭要素は{scores2[0]}")

print("変数scores2の中身を変数scores1に代入(コピー)します")

scores1 = scores2

print("scores1の先頭要素を90に書き換えます")

scores1[0] = 90

print(f"90を代入したscores1の先頭要素は{scores1[0]}")
print(f"90を代入していないscores2の先頭要素は{scores2[0]}")

# scores1 = scores2ではidentity値が参照コピーされるため、同じオブジェクトが実行される状態になる（詳細：p246）
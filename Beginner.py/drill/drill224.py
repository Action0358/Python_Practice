# コード2-5 試験の合計と平均を求める
# ネットワーク、データベース、セキュリティ試験の点数
scores = [88, 90, 95]

total = scores[0] + scores[1] + scores[2]
print(f"合計{total}点")

# コード2-6 sum関数を用いて合計を求める
scores = [88, 90, 95]

total = sum(scores)
print(f"合計{total}点")

# コード2-7 リストの合計値と平均値を求める
scores = [88, 90, 95]

total = sum(scores)
avg = total / len(scores) #len関数はリストの要素数を求める
print(f"合計点{total}点, 平均点{avg}点")
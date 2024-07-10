#コード2-23 コンテナの相互変換
scores = {"network": 60, "database": 80, "security": 60}
members = ["松田", "浅木", "工藤"]

print(tuple(members)) #リストmemberをタプルに変換して表示
print(list(scores)) #scoresのキーをリスト変換して表示
print(set(scores.values())) #scoresの値をセットに変換して表示

#ディクショナリ.values()は、キーを除いた値だけからなる集まり


# コード4-11 不要な回のループをスキップする
ages = [28, 50, "ひみつ", 20, 78, 25, 22, 10, "無回収", 33]
samples = list() # サンプルデータを格納するリスト
for data in ages:
    if not isinstance(data, int): # 整数でないデータはスキップ
        continue
    
    if data < 20 or data >= 30: # 目的の条件に合致しないデータはスキップ
        continue
    
    samples.append(data)

print(samples)

# isinstance() = isinstance関数は1番目の引数に指定したデータが2番目の引数に指定したデータ型と等しいかどうかを返す
# データ型にはint, str, bool型など指定できる
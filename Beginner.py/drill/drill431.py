# コード4-9 データのまとまりからサンプルを抽出する
ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33] # 対象データ
num = 5 # 目標の抽出数
samples = list() # サンプルデータを格納するリスト

for age in ages:
    if 20 <= age < 30:
        if len(samples) < num: # 要素番号は0からカウントする
            samples.append(age)      
    else:
        pass
    
print(samples)

# コード4-10 目標数に達したら繰り返しを終了する
ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33] # 対象データ
num = 5 # 目標の抽出数
samples = list() # サンプルデータを格納するリスト

for data in ages:
    if 20 <= data < 30:
        samples.append(data)
        if len(samples) == num: # 抽出数が目標に達したので、for文を強制終了
            break
           
print(samples)

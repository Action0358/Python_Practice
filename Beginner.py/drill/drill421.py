# コード4-7 for文でリストの全要素を参照する
# データの集まりから要素を取り出して、それに対する処理を繰り返す
scores = [80, 20, 75, 60]

for data in scores:
    
    if data >= 60:
        print("合格")
    
    else:
        print("不合格")
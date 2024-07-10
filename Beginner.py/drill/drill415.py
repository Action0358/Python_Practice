# コード 4-6 リストの全要素を繰り返し
scores = [80, 20, 75, 60]
count = 0

while count < len(scores): # リストや文字列など様々な型のオブジェクトのサイズ（要素数や文字数）を取得できる
    
    if scores[count] >= 60:
        print("合格")
    
    else:
        print("不合格")
    
    count += 1
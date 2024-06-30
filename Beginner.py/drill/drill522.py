# コード5-7 複数の引数を渡す
def profile(name, age, hobby): # 関数定義
    print(f"私の名前は{name}です。") # 処理
    
    print(f"年齢は{age}です。") # 処理
    
    print(f"趣味は{hobby}です。") # 処理
    
# 引数は、呼び出し時に記述した順に従って受け取られる
profile("浅木", "24", "カフェ巡り") # 複数の引数を渡す


# コード5-8 リストの平均を求める calc_average関数
scores = [100, 80, 70, 90, 60]

def calc_average(scores): # リストを受け取る引数
    avg = sum(scores) / len(scores) # 受け取ったリストに格納されている得点の平均を求める
    
    print(f"平均点は{avg}です")

calc_average(scores)
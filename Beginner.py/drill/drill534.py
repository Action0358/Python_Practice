# コード5-19 おやつも食べた日のeat関数の呼び出し
def eat(breakfast, lunch, dinner = "カレー", desserts = ()): # 要素数0のタプルをデフォルト引数に指定
    print(f"朝は {breakfast}を食べました")
    
    print(f"昼は{lunch}を食べました")
    
    print(f"夜は{dinner}を食べました")
    
    for d in desserts:
        print(f"おやつに{d}を食べました")
        
eat("トースト", "パスタ", "カレー", ("アイス", "チョコ", "パフェ")) # おやつの部分は丸カッコで囲んでタプルにする


# コード5-20 おやつも食べた日のeat関数の呼び出し(可変長引数を利用)
def eat(breakfast, lunch, dinner="カレー", *desserts): # dessertsは可変長引数を表明
    print(f"朝は {breakfast}を食べました")
    print(f"昼は{lunch}を食べました")
    print(f"夜は{dinner}を食べました")
    
    for d in desserts:
        print(f"おやつに{d}を食べました")

eat("トースト", "パスタ", "カレー", "アイス", "チョコ", "カレー") # おやつの部分が１つのタプルとして仮引数dessertsに引き渡される


# ディクショナリを用いた可変長引数
def eat(**kwargs):
    for key in kwargs: # for文にディクショナリを指定するとキーが順番に取り出される
        
        print(f"{key}に{kwargs[key]}を食べました")

eat(朝食 = "納豆", 遅めの昼食 = "パスタ", 夕方のおやつ = "カレーパン" ) # この部分が１つのディクショナリとして引数kwargsに渡される

# 可変長引数がタプルの場合は仮引数を *argsとする習慣がある
# 可変長引数がディクショナリの場合は仮引数を *kwargsとする習慣がある
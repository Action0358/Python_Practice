# コード5-19 おやつも食べた日のeat関数の呼び出し
def eat(breakfast, lunch, dinner = "カレー", desserts = ()):
    print(f"朝は {breakfast}を食べました")
    
    print(f"昼は{lunch}を食べました")
    
    print(f"夜は{dinner}を食べました")
    
    for d in desserts:
        print(f"おやつに{d}を食べました")
        
eat("トースト", "パスタ", "カレー", ("アイス", "チョコ", "パフェ"))


# コード5-20 おやつも食べた日のeat関数の呼び出し(可変長引数を利用)
def eat(breakfast, lunch, dinner="カレー", *desserts):
    print(f"朝は {breakfast}を食べました")
    print(f"昼は{lunch}を食べました")
    print(f"夜は{dinner}を食べました")
    
    for d in desserts:
        print(f"おやつに{d}を食べました")

eat("トースト", "パスタ", "カレー", "アイス", "チョコ", "カレー")

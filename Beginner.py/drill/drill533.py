# 5-17 夜がカレーじゃない日のeat関数の呼び出し
def eat(breakfast, lunch = "ラーメン", dinner = "カレー"):
    print(f"朝は{breakfast}を食べました")
    
    print(f"昼は{lunch}を食べました")
    
    print(f"夜は{dinner}を食べました")
    
eat("納豆ごはん", "ラーメン", "カレーうどん")

# 引数のキーワード指定
# デフォルト引数の関係上、第２引数を省略せずに渡す


# コード5-18 夜がカレーじゃない日のeat関数の呼び出し（キーワード指定）
eat(breakfast = "納豆ごはん", dinner = "カレーうどん")
eat(dinner = "カレーうどん", breakfast = "納豆ごはん")
eat("納豆ごはん", dinner = "カレーうどん")

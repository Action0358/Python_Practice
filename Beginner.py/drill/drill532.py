# コード5-15 松田くんの食生活を表示する
def eat(breakfast, lunch, dinner):
    print(f"朝は{breakfast}を食べました")
    print(f"昼は{lunch}を食べました")
    print(f"晩は{dinner}を食べました")
    
print("8月1日")
eat("トースト","おにぎり","カレー")

print("8月2日")
eat("納豆ごはん", "ラーメン", "カレー")

print("8月3日")
eat("バナナ", "そば", "焼肉")

print("8月4日")
eat("サンドウィッチ", "しゅうまい弁当", "カレー")


# 5-16 松田くんの言うまでもない食生活を表示する
def eat(breakfast, lunch, dinner = "カレー"):
    print(f"朝は{breakfast}を食べました")
    print(f"昼は{lunch}を食べました")
    print(f"晩は{dinner}を食べました")
    
print("8月1日")
eat("トースト","おにぎり")

print("8月2日")
eat("納豆ごはん", "ラーメン")

print("8月3日")
eat("バナナ", "そば", "焼肉")

print("8月4日")
eat("サンドウィッチ", "しゅうまい弁当")


# デフォルト引数の制約
# def eat(breakfast = "トースト", lunch, dinner):
# デフォルト引数を使用する場合は、必ず一番後ろの引数から順にデフォルト値を指定


# コード3-8 elseブロックのない分岐
name = input("あなたの名前を教えてください >>")
print(f"{name}さん、こんにちは")

if name == "松田": # nameが松田ではないときの処理はない
    print("松田さんに会えて嬉しいです")
    
food = input(f"{name}さんの好きな食べ物を教えてください >>")

if "カレー" in food:
    print("素敵です。とにかくカレーは最高ですよね!!")
    
else:
    print(f"私も{food}が好きですよ")

# 空のブロックの作り方
name = input("あなたの名前を教えてください >>")
print(f"{name}さん、こんにちは")

if name == "松田": # nameが松田ではないときの処理はない
    print("松田さんに会えて嬉しいです")
    
food = input(f"{name}さんの好きな食べ物を教えてください >>")

if "カレー" in food:
    print("素敵です。とにかくカレーは最高ですよね!!")
    
else:
    pass # ブロックの中身を空にしたい場合は、passと表記

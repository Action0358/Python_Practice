# コード3-1 いつもと同じことを言うチャットボット
# name = input("あなたの名前を教えてください >>") # 引数入力
# print(f"{name}さん、こんにちは")
# food = input(f"{name}さんの好きな食べ物を教えてください >>") # 引数入力
# print(f"私も{food}が好きなんですよ")

# コード3-2 答えが分岐するチャットボット
name = input("あなたの名前を教えてください >>")
print(f"{name}さん、こんにちは")

food = input(f"{name}さんの好きな食べ物を教えてください >>")

if food == "カレー":
    print("素敵です。カレーは最高ですよね！！") 
 
else:
    print(f"私も{food}が好きですよ")


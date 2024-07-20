def welcome(u):
    print(f"ようこそ{u["name"]}さん")
    
    u["age"] = u["age"] + 1 # ミュータブル
    
    print(f"あなたは来年{u["age"]}歳だから大吉です！")
    
username = input("名前を入力してください >>")
userage = int(input("年齢を入力してください >>"))

user = {"name" : username, "age" : userage}

copied_user = user.copy()
welcome(copied_user)

print(f"{user["age"]}歳の{user["name"]}さん、またプレイしてくださいね")    

# 関数内にreturnがなく、ミュータブルであることから、user["age"]に直接変更が反映されている。そのため、防御的コピーより元の変数に影響を及ぼさない
# コード3-4 どんなカレーでも絶賛するチャットボット(in演算子)
name = input("あなたの名前を教えてください >>")# 引数入力
print(f"{name}さん、こんにちは") 

food = input(f"{name}さんの好きな食べ物を教えてください >>")# 引数入力

if "カレー" in food:
    print("素敵です。カレーは最高ですよね！！")
       
else:
    print(f"私も{food}が好きですよ")

# コード3-5 100点があるかどうか調べる
scores = [80, 100, 20, 60]

if 100 in scores:
    print("100点満点の試験があったんですね。おめでとう!")   
 
else:
    print("次はどれか1つでも100点満点を取ろう")
    

# コード3-6 ディクショナリのキーをチェックする
scores = {"network": 60, "database": 80, "security": 50}
key = input("追加する科目名を入力してください >>") # 引数入力

if key in scores:
    print("すでに登録済みです")
    
else:
    data = int(input("得点を入力してください >>")) # 引数入力
    scores[key] = data
print(scores)

# 文字列の大小比較
# 例えば、aとbではbの方が大きく、pythonとpayではpythonの方が大きいと判定される
# 具体的には、「松田」の「松」と「浅木」の「浅」を比較する。それぞれのUnicodeコードポイントの値が判定される。
# 松 =  U+677E = 26462, 浅 = U+6D45 = 27973
name = "松田"

if name < "浅木":
    print("条件が成立")
    
else:
    print("条件が成立しない")
    
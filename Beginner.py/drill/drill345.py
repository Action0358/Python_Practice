# # 晩御飯をレコメンドするチャットボット
# # if文のネスト
# .strip()メソッドは、文字列の先頭と末尾からすべての空白文字（スペース、タブ、改行など）を削除する。
# .lower()メソッドは、文字列のすべての文字を小文字に変換する

print("すべての質問に y または n で答えてください")

okane_aruka = input("お金に余裕はありますか >>").strip().lower()

if okane_aruka == "y":
    onaka_suiteruka = input("お腹がすごく空いていますか？ >>").strip().lower()
    nomitai_kibunka = input("ビールを飲みたいですか？ >>").strip().lower()
    
    if onaka_suiteruka == "y" and nomitai_kibunka == "y":
        print("焼肉はいかがですか")
        
    elif onaka_suiteruka == "y":
        print("カレーはいかがですか")
        
    elif nomitai_kibunka == "y":
        print("焼き鳥はいかがですか")
        
    else:
        print("パスタはいかがですか")
        
else:
    print("家で食べましょう")

# 夜食の質問はお金の余裕があるかどうかに関係なく尋ねる
yashoku_iruka = input("夜食は必要ですか？ >>").strip().lower()

if yashoku_iruka == "y":
    print("コンビニのチキンはいかがですか")

else:
    pass

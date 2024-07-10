# コード4-4 眠るまでひつじを数えるのを繰り返す
# bool型でフラグを表す、変数名はis_xxxとするのが一般的
is_awake = True
count = 0

while is_awake == True:
    count += 1
    
    print(f"ひつじが{count}匹")
    
    key = input("もう眠りそうですか？(y/n) >>").strip().lower() # 引数入力
    
    if key == "y":
        is_awake = False
        
print("おやすみなさい")
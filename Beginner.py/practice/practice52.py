def is_leapyear(y):
    return(y % 400 == 0 or (y % 4 == 0 and y % 100 != 0))

current_year = int(input("現在の西暦を入力してください >>"))

if is_leapyear(current_year):
    print(f"西暦{current_year}年は、うるう年です")
    
else:
    print(f"西暦{current_year}年は、うるう年ではありません")
    

# 関数の定義＝1行目、関数の呼び出し＝6行目  
# 関数を呼び出すときに引数を指定すると、その値は関数内でその引数名として使用されるため、current_yearがyに引き渡された



# 以下の引数名を統一することで、コードの一貫性が高まり、可読性が向上する

# def is_leapyear(current_year):
#     return(current_year % 400 == 0 or (current_year % 4 == 0 and current_year % 100 != 0))

# current_year = int(input("現在の西暦を入力してください >>"))

# if is_leapyear(current_year):
#     print(f"西暦{current_year}年は、うるう年です")
    
# else:
#     print(f"西暦{current_year}年は、うるう年ではありません")
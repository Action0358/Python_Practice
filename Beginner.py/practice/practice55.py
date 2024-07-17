# 計算データの入力
amount = int(input("支払総額を入力してください >>"))
people = int(input("参加人数を入力してください >>"))

# 割り勘の計算
dnum = amount / people # 総額を人数で割る (端数も保持)
pay = dnum // 100*100 # 100円未満を切り捨てる

if dnum > pay: # 元の値と比較して
    pay = int(pay + 100) # 小さければ100円未満があったので上乗せ

# 幹事の支払額の計算
payorg = amount - pay * (people - 1)

# 結果の表示
print("*** 支払額 ***")
print(f"1人あたり{pay}円({people}人)、幹事は{payorg}円です")





def int_input(msg):
    return int(input(f"{msg}を入力してください >>"))

def calc_payment(amount, people = 2):
    dnum = amount / people # 総額を人数で割る (端数も保持)
    pay = dnum // 100 * 100 # 100円未満を切り捨てる
    
    if dnum > pay: # 元の値と比較して
        pay = pay + 100 # 小さければ100円未満があったので上乗せ
    
    payorg = amount - pay * (people - 1)
    return [int(pay), int(payorg)]

def show_payment(pay, payorg, people = 2):
    print("*** 支払額 ***")
    
    print(f"1人あたり{pay}円({people - 1}人)、幹事は{payorg}円です")
    

# 計算データ入力
amount = int_input("支払総額"); people = int_input("参加人数")

# 割り算結果
[pay, payorg] = calc_payment(amount, people)

# 結果表示
show_payment(pay, payorg, people)
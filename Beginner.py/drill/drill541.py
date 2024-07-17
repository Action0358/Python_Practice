# # コード5-21 引数を使わずに変数nameの値を受け渡ししている
# name = "松田"

# def hello():
#     print("こんにちは" + name + "さん")

# hello()

# # 関数は外の世界から独立しており、引数や戻り値を使わなければ外の世界とデータやり取りできない

# # グローバル変数
# # 全ての関数から参照してデータを利用できる
# # 同名のローカル変数がある場合、ローカル変数が優先して利用される


# # コード5-22 関数の中からグローバル変数に代入できる
# name = "松田"

# def change_name():
#     name = "浅木"
    
# def hello():
#     print("こんにちは" + name + "さん")
    
# change_name()
# hello()


# コード5-23 global文を用いてグローバル変数に代入する
# name = "松田"  # グローバル変数 name を定義

name = "松田"  # グローバル変数 name を定義

def change_name():
    global name  # グローバル変数 name を関数内で使うことを宣言
    name = "浅木"  # グローバル変数 name を変更

def hello():
    print("こんにちは" + name + "さん")  # 現在のグローバル変数 name の値を使って挨拶

# グローバル変数 name の初期値を使用して挨拶
hello()  # 出力: こんにちは松田さん

# グローバル変数 name を変更
change_name()

# 変更後のグローバル変数 name を使用して挨拶
hello()  # 出力: こんにちは浅木さん

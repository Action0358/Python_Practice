# コード5-3 hello関数の定義
def hello():
    print("こんにちは。工藤です。")

# hello関数を作成して利用できるようにしたのみ

# コード5-4 hello関数の定義と呼び出し
def hello():
    print("こんにちは。工藤です。") # 関数ブロック
    
hello()

# オリジナル関数を使うには、定義(definition)と呼び出し(call)が必要
# 関数の定義は呼び出されたらどのような動作を行うかを記述し、名前をつける
# 関数の呼び出しは関数の名前を記述して関数を呼び出す（定義された動作が実行される）

# 関数名の衝突による上書き
# すでに定義されている関数と同じ名前を付けると、以前の関数は呼び出せなくなる
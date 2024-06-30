# コード5-5 input_scores関数の変数nameに代入するつもり
def input_scores(name):
    print(f"{name}の試験結果を入力してください")
    
input_scores("浅木")
input_scores("松田")

# ローカル変数は関数の中で定義された変数
# その関数が外や他の関数の中に偶然同じ名前の変数があったとしても、全く無関係な別の存在として扱われる
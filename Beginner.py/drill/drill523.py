# コード5-9 input_scores関数とcalc_average関数
def input_scores(name):
    print(f"{name}さんの試験結果を入力してください")
    
    network = int(input("ネットワークの得点？ >>"))
    database = int(input("データベースの得点？ >>"))
    security = int(input("セキュリティの得点？ >>"))
    
    scores = [network, database, security] # ローカル変数の独立性(input_score関数内に変数scoreの処理が存在しない)
    return scores # scoresリストに入力した値を返す
    
def calc_average(scores):
    avg = sum(scores) / len(scores)
    
    print(f"平均点は{avg}です")

scores = input_scores("浅木") # input_scores関数の戻り値をscoresに格納
calc_average(scores) # scoresをcalc_average関数に渡す


# scores = input_scores("浅木")は、def calc_average(scores)の（）内の引数に渡されinput_scores関数内の処理が呼び出される

# 引数と戻り値を利用する関数の定義
# def 関数名(引数):
#     処理
#     return (戻り値) 引数は複数の指定が可能だが、戻り値は１つのみ



# コード5-11 足し算の結果を返すplus関数
def plus(x, y):
    answer = x + y
    
    return answer

answer = plus(100, 50) # 変数名は任意であるが、ここでは一貫性を持たせるために answer を使用している(関数内の変数 answer と戻り値を受け取る変数 answer を統一することで、何が計算されて返ってくるのかが明確になる)
print(f"足し算の答えは{answer}です") # 戻り値を受け取る変数 answerをprint関数に渡している


# 下記のコードのようにresultはローカル変数のためprintで表示することができない
# def plus(x, y):
#     result = x + y
    
# plus(100, 50)
# print(f"足し算の答えは{result}です")



# 戻り値（返り値）とは、プログラム中で呼び出された関数などが処理を終了する際に、呼び出し元に対して渡す値のこと
# returnは、処理された結果（戻り値）を何らかの形で、他の関数で利用したいという場合に使う

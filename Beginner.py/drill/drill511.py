# コード5-1 見通しの悪いプログラム
student_list = ["浅木", "松田"]

for student in student_list:
    print(f"{student}さんの試験結果を入力してください")
    
    scores =list()

# while文を用いた真偽
    while True:
        # try-except = エラーが発生する可能性のあるコードを実行し、エラーが発生した場合に特定の処理を行う(例外処理)
        try:
            network = int(input("ネットワークの得点？ >>"))
            database = int(input("データベースの得点？ >>"))
            security = int(input("セキュリティの得点？ >>"))
            
            if not (0 <= network <= 100 and 0 <= database <= 100 and 0 <= security <= 100):
                print("得点は0から100の間で入力してください。")
                continue
            
            scores.append(network)
            scores.append(database)
            scores.append(security)
            break
        
        except ValueError:
            print("正しい数値を入力してください。")
    
    if student == "浅木":
        asagi_scores = [network, database, security]
        asagi_avg = sum(asagi_scores) / len(asagi_scores)

    else:
        matsuda_scores = [network, database, security]
        matsuda_avg = sum(matsuda_scores) / len(matsuda_scores)
        
print(f"浅木さんの平均値は{asagi_avg}です")
print(f"松田さんの平均値は{matsuda_avg}です")



# コード5-2 見通しが良くなったプログラム
# 得点入力
# asagi_scores = input_scores("浅木")
# matsuda_scores = input_scores("松田")

# # 平均点を計算
# asagi_avg = calc_average(asagi_scores)
# matsuda_avg = calc_average(matsuda_scores)

# # 結果を出力
# output_result("浅木", asagi_avg)
# output_result("松田", matsuda_avg)

# 関数は使うだけでなく作成することができる
# input_scoresやcalc_averageは作成した関数になる
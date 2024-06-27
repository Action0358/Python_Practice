# 九九の計算(奇数の段のみ)
# 掛け算の答えが50を超えたら計算を中止

results = {} # 空の辞書を定義

for x in range(1, 10): # 1以上9未満
    if x % 2 == 0:
        continue
    
    results[x] = []  #  x が奇数の場合、辞書にキー x を追加し、空のリストを値として初期化 → コード2-15参照
    
    for y in range(1, 10): # 1以上9未満
        if x * y > 50:
            break
        
        results[x].append(x * y)
        
print(results)

# 具体例を使った説明
# x が 3 のとき、 if x % 2 == 0: によってスキップされないので、次の処理に進みます。
# results[3] = [] によって、 results 辞書にキー 3 を持つエントリが追加され、その値として空のリストが初期化されます。
# 内側のループ for y in range(1, 10): で y が 1 から 9 までの値を順に取ります。
# if x * y > 50: で x * y が 50 を超える場合に内側のループを抜けるため、 3 * y が 50 を超えるまで以下の処理が繰り返されます。
# results[3].append(x * y) によって 3 * y の結果がリスト results[3] に追加されます。
# これを他の奇数（1, 5, 7, 9）についても同様に行います。

# 最終的に、 results 辞書には次のようなデータが格納されます
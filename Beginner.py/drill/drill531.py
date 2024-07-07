# コード5-13 2つの戻り値を返す
# def plus_and_minus(a, b):
#     return a + b , a - b

# next, prev = plus_and_minus(1978, 1)


# コード5-14 戻り値のタプルをアンバック代入
def plus_and_minus(a, b):
    return(a + b, a - b) # 要素数2のタプルを1つ返している

(next, prev) = plus_and_minus(1978, 1) # 返ってきたタプルをアンバック代入している

print(next, prev)

# アンバック代入は、変数をカンマで区切ってまとめて代入する方法（カンマで区切られた値はタプルを意味する）
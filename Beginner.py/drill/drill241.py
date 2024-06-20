#コード2-17 タプルの利用
#リストとほぼ同じ特徴だが、要素の追加、変更、削除ができない
#タプルは()カッコで定義する
scores = (70, 80, 55)
print(scores)
print(scores[0])
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')

#コード2-19 要素数1の型
members = ('松田')
print(type(members))

#コード2-20 要素数1の型
#タプルを生成する記号は丸カッコではなくカンマ
members = ('松田',)
print(type(members))


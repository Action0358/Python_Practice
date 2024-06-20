#コード2-22 セットの利用
#重複した値を持つことができない
#添え字やキーの概念がないため、要素は順序を持たない
#add関数で要素を追加する
scores = {70, 80, 55, 80}
scores.add(80)
print(scores)
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')
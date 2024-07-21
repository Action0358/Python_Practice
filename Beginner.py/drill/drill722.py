# コード7−1 1行日記を記録する
text = input("何を記録しますか？ >>")

file = open("diary.txt", "a" )
file.write(text + "\n" )
file.close()

# このプログラムを実行すると同じフォルダ内にテキストファイル（diary.txt）が作成される


# コード7-2 用が済んだらすぐに閉じる
text = input("今日は何した？ >>")
with open("diary.txt", "a") as file:
    file.write(text + "\n")

# このプログラムを実行すると同じフォルダ内にテキストファイル（diary.txt）が作成される
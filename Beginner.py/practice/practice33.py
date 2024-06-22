# (1) 変数isErrorがFalseかつ変数nが100未満の場合のみ、画面表示を行う(表示内容は問わない)
isError = False
n = 99
if isError == False and n < 100:
    print("正解です")
    
# (2) 入力された数値について、偶数か奇数かを判定してその結果を表示する
number =int(input("数値を入力してください >>"))

if number % 2 == 0:
    print("偶数です")

else:
    print("奇数です")
    
# (3) 入力された次の文字列に応じて、挨拶を表示する
greeting = input("挨拶をどうぞ >>")

if greeting == "こんにちは":
    print("ようこそ")

elif greeting == "景気は？":
    print("ぼちぼちです")

elif greeting == "お元気で!":
    print("お元気で!")

else:
    print("どうしましたか")
    
# (4) 
month = int(input("今日は何月ですか？ >>"))

if month in [1, 3, 5, 7, 10, 12]:
    print("31日までありますね")
    
else:
    if month != 2:
        print("30日までですね")
    
    else:
        print("1年で一番寒い月ですね")
    
    print("年が明けてから")

print(f"{month}か月が過ぎました")        
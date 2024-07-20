# コード6-8 関数に変数の内容を書き換えれてしまう
def add_suffix(names): # namesは仮引数のため、今回before_namesが引数で渡された際。namesが全てbefore_namesに置き換わる
    for i in range(len(names)):
        names[i] = names[i] + "さん"
    
    return names # returnは関数内で処理された内容をbefore_namesに直接反映させている。ただし、今回は関数内の操作が直接 before_names に影響を与えているため、return の役割は特に重要ではない

before_names = ["松田", "浅木", "工藤"] #　関数内の処理がbefore_namesに反映させているため、"さん"が付く
after_names = add_suffix(before_names) 

print("さん付け後: + after_names[0]" )
print("さん付け前: + before_names[0]" )
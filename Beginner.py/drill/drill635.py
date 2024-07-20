# コード6-10 文字列を渡しても悪影響が起きない
def add_suffix(name):
    name = name + "さん"
    
    return name

before_name = "松田"
after_name = add_suffix(before_name)

print("さん付け後" + after_name)
print("さん付け前" + before_name)


# コード6-11 identity値の変化の比較
print("identityの変化を比較")

names = list()
print(f"list(変更前) : {id(names)}")

names.append("松田")
print(f"list(変更後) : {id(names)}")

name = "松田"
print(f"str(変数前) : {id(name)}")

name = "スーパー" + name
print(f"str(変更後) : {id(name)}")
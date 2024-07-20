# コード6-9　防御的コピーを用いて悪影響を防ぐ
def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + "さん" # 変数names[i] を使う理由: リストの特定の要素にアクセスして変更するため
    
    return names

before_names = ["松田", "浅木", "工藤"]
copied_names = list()

for n in before_names:
    copied_names.append(n)

after_names = add_suffix(copied_names)

print("さん付け後:" +  after_names[0])
print("さん付け前：" +  before_names[0])

# names = names[i] + "さん" がダメな理由: リスト全体ではなく、変数 names が単なる文字列に置き換わってしまうため

# ループの初回 (i = 0):
# names = names[0] + "さん" は "松田さん" となり、names 変数にその値が代入される
# この時点で names はリストではなく、単なる文字列 "松田さん" になる

# 2回目のループ (i = 1):
# 既に names はリストではなく文字列なので、names[i] はエラーを引き起こす。リストのインデックスで文字列にアクセスしようとするため


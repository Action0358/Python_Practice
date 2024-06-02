#  コード1-27 f-stringで文字列に数値を埋め込む
name = "松田光太"
age = 23
height = 175.6
print(f'私の名前は{name}で、年齢は{age}歳で、身長は{height}cmです')

# column f-stringでの評価式付き表示
hp, maxHp = 80, 100
print(f'{hp} / {maxHp}')
print(f'{hp = } / {maxHp = }')
print(f'{hp / maxHp = }')

# コード1-9 同じ式が何度も登場してしまう
print("半径が3cmの円の直径は、")
print(3 * 2)
print("その円の円周の長さは、直径×円周率でも求まるため、")
print(3 * 2 * 3.14)

# コード1-10 変数の利用
name = "松田"
age = 22
print(name)
print(age)

# コード1-11 変数を利用してコード1-9を改善
print("半径が3cmの円の直径は、")
dia = 3 * 2  # dia = diameter 
print(dia)
print("その円の円周の長さは、")
print(dia * 3.14)
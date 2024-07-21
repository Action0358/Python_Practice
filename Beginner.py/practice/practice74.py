nums = list()
for n in range(3):
    data = int(input(f"{n + 1}個目の整数を入力してください >>"))
    
    nums.append(data)

print(max(nums))


pi = 3.141519
print(round(pi))

for n in range(4):
    print(round(pi, n + 1))
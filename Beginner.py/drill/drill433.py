# break文とcontinue文
# break文
data_list = [1, 2, 3]
samples = list()

for num in data_list:
    if num == 2:
        break
    
    samples.append(num)
    
print(samples)
    
# continue文
data_list = [1, 2, 3]
samples = list()

for num in data_list:
    if num == 2:
        continue
    
    samples.append(num)

print(samples)
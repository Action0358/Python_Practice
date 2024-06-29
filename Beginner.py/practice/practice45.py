import math

# key = 時刻、value = 気温
dict = {"8時": 7.8, "9時": 9.1 , "10時": 10.2 , "11時": 11.0, "12時": 12.5 , 
        "13時": 12.4, "14時": 14.3, "15時": 13.8, "16時": 12.9, "17時": 12.4}

temp = list()

# 値のみループ処理する場合は、.item() メソッドを使用
for value in dict.values():
    temp.append(value)
    
print(temp)


temp_new = list()

# key 13時の値を変更
dict["13時"] = "N/A"

# 値のみループ処理をする場合は、.value() メソッドを使用
for value in dict.values():
    temp_new.append(value)

print(temp_new)


total = 0

for val in temp_new:
    if isinstance(val, (int,float)):
        total += val

print(str(total))  

# 平均値を算出
avg = total / (len(temp_new) - temp_new.count("N/A"))

# mathモジュールにより、切り上げceil()メソッドが使用できる(切り捨て＝floorメソッド)
print(math.ceil(avg)) # print(round(avg))を使用して四捨五入することも可能



# # キーと値をセットでループ処理する場合は、.items() メソッドを使用
# for key, value in dict.items():
#     print(key, value)



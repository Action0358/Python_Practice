a = 70
b = 50

scores = [ 90, 60, 40, 0, a, b, ]

for x in scores:
    if x >= 60:
        print("合格です")
    
    elif 30 <= x < 60:
        print("追試です")
    
    else:
        print("不合格です")
        
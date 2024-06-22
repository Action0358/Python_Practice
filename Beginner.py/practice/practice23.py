member_hobbies = {
    "松田" : {"映画", "温泉", "ドライブ", "読書", "音楽"},
    "浅木" : {"映画", "スポーツ", "音楽", "食べ歩き", "旅行"}
}

common_hobbies = member_hobbies["松田"] & member_hobbies["浅木"]
total_hobbies = member_hobbies["松田"] | member_hobbies["浅木"]

matching =  len(common_hobbies) / len(total_hobbies) *100

print("心の準備ができたらEnterキーを押してください")
print(f"相性度{matching}%")
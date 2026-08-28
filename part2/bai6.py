scores = {
    "Bin": 8.5,
    "An": 7.0,
    "Nam": 9.0,
    "Lan": 6.5
}
# 1. In tất cả tên
for name in scores:
    print(name)
# 2. In tất cả điểm
for score in scores.values():
    print(score)
# 3. Tìm sinh viên có điểm cao nhất
max_score = max(scores.values())
for name, score in scores.items():
    if score == max_score:
        print("Sinh viên điểm cao nhất:", name, score)
# 4. Tìm sinh viên có điểm thấp nhất
min_score = min(scores.values())
for name, score in scores.items():
    if score == min_score:
        print("Sinh Vien diem thap nhat: ", name, score)

# 5. Tạo dictionary mới chứa sinh viên có điểm >= 8
high_scores = {
    name: score
    for name, score in scores.items()
    if score >= 8
}
print(high_scores)

list_score = {}
for name, score in scores.items():
    if score >= 8:
        list_score[name] = score
print(list_score)
    



students = [
    {"name": "A", "score": 8},
    {"name": "B", "score": 5},
    {"name": "C", "score": 9}
]
# In sinh viên điểm cao nhất
max_score = None
max_student = None
for i in students:
    if max_score is None or i["score"] > max_score:
        max_score = i["score"]
        max_student = i["name"]
print("studen max score:", max_student, " ", max_score)
# Lọc sinh viên >= 8
good_student = []
for i in students:
    if i["score"] >= 8:
        good_student.append(i)
print("students score than 8:", good_student)
# Tính điểm trung bình
total = 0;
count = 0;
for i in students:
    total += i["score"]
    count += 1
print("average score:",total/count)
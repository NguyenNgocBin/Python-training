students = {
    "A": 8,
    "B": 5,
    "C": 9
}
# In học sinh điểm cao nhất
max_student = None;
max_score = 0;
for name in students:
    if (students[name] >  max_score):
        max_score = students[name]
        max_student = name
print(max_student, max_score)
# Tính điểm trung bình
medium = 0;
count = 0;
for name in students:
    medium += students[name]
    count += 1
print(medium/count)
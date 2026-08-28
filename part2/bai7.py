students = [ # student is list not dictionary
    {"name": "Bin", "age": 20, "gpa": 3.2}, #i0
    {"name": "An", "age": 21, "gpa": 3.6}, #i1
    {"name": "Nam", "age": 20, "gpa": 2.8}, #i2
    {"name": "Lan", "age": 19, "gpa": 3.9} #i3
]
for i in students:
    print(i["name"], "-", i["age"], "-", i["gpa"])

max_gpa = max(i["gpa"] for i in students)

for i in students:
    if i["gpa"] == max_gpa:
        print("Best student: ", i["name"])
        print("GPA: ", i["gpa"])
# tinh gpa tb
tb = sum(i["gpa"] for i in students)/len(students)
print("GPA trung bình:", tb)
# loc loai kha
kha = []
for i in students:
    if i["gpa"] >= 3.0:
        kha.append(i)
print(kha)

# Viết function student_info(**kwargs) in ra từng key và value.
# output
# name: Bin
# age: 20
# major: IT

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
student_info(
    name="Bin",
    age=20,
    major="IT"
)
student_info(
    name="BinDZ",
    age=21,
    major="Information Teachnololy"
)

# Viết function total(*args) nhận bao nhiêu số cũng được và trả về tổng.

def total(*args):
    total = 0
    for i in args:
        total += i
    return total
print(total(1, 2, 3, 4))
#return sum(args) cách viết nhanh
S = "banana"
# Đếm số lần xuất hiện mỗi ký tự
# output{'b':1, 'a':3, 'n':2}
count = {} # khởi tạo dict
for i in S:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

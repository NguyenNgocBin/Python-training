l = [1, 2, 3, 4, 5]
# In phần tử đầu và cuối
print(l[0])
print(l[-1])
# Tính tổng list
sum = 0
for i in l:
    sum += i
print(sum)
# Thêm số 10 vào cuối list
l.append(10)
print(l[-1])
# Xóa phần tử thứ 2
l.remove(2)
for i in l:
    print(i)
    
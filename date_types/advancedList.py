L = [1, 2, 3, 4, 5, 6]
# Lấy các số chẵn
for i in L:
    if(i % 2 ==0):
        print(i)
#Tạo list mới chứa bình phương các số
N = []
for i in L:
    i *= 2
    N.append(i**2)

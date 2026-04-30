# Viết function find_max(numbers) trả về số lớn nhất trong list.

def find_max(number):
    s = number[0]
    for i in number:
        if(i > s):
            s = i
    return s
print(find_max([1, 2, 3, 4, 5, 9, 2, 1]))

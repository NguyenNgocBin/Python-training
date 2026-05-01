# Viết function filter_even(numbers) trả về list chỉ chứa số chẵn.

def filter_even(numbers):
    a = []
    for i in numbers:
        if i % 2 == 0:
            a.append(i)
    return a
print(filter_even([2, 3, 4, 5, 6, 7]))
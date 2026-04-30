# Viết function count_even(numbers) trả về số lượng số chẵn trong list.

def cout_even(numbers):
    cout = 0
    for i in numbers:
        if i % 2 == 0:
            cout += 1
    return cout
print(cout_even([1, 2, 3, 4, 5, 6]))
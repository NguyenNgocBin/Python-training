# Viết function is_even(n) trả về:
# True nếu n là số chẵn
# False nếu n là số lẻ

def is_even(n):
    if n % 2 == 0:
        return True
    else: 
        return False
print(is_even(5))
print(is_even(6))
# cách pro hơn 
# def is_even(n)
#       return n % 2 == 0
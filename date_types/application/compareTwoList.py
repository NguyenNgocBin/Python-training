A = [1, 2, 3, 4]  # & toán tử giao
B = [3, 4, 5, 6] 
# Phần tử chung
common = list(set(A) & set(B))
print(common)
# Phần tử riêng từng list
Only_A = list(set(A) - set(B))
Only_B = list(set(B) - set(A))
print(Only_A)
print(Only_B)
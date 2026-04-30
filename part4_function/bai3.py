# Viết function average(scores) nhận vào một list điểm và trả về điểm trung bình.
def average(score):
    if len(score) == 0:
        return 0
    return sum(score)/len(score)
print(average([1, 2, 3, 4, 5]))
try:
    age = int(input("Age: "))

except ValueError as e:
    print("Exception type:", type(e))
    print("Exception message:", e)
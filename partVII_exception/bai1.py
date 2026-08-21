try: 
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = a / b
except ValueError:
    print("Plese Enter number")
except ZeroDivisionError:
    print("Error: Can't divide zero")
else:
    print("Result: ",result)
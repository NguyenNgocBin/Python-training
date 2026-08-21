def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Logging error...")
        raise # ném error ra ngoai
try:
    divide(10, 0)
except ZeroDivisionError:
    print("handle outside")
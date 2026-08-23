class InsufficientBalanceError(Exception): #create a custom exception to represent an "insufficient balance" error.
    pass

def withdraw(blance, amount):
    if amount > blance:
        raise InsufficientBalanceError("Insufficient balance")
    else:
        print("Withdrawal successful")
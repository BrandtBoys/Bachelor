def mul(a,b):
    # This function multiplies two numbers using a recursive approach.
    # It works by repeatedly applying the multiplication operation to the result so far and the current number.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
        # The result is updated by multiplying it with the current number, then the current number is decremented.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # This function subtracts two numbers and prints "Test print" for demonstration purposes.
    # It simply returns the difference between the two numbers.
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is enough balance to do something by subtracting the amount from the current balance.
    # It returns True if the result is greater than 0 (i.e., there is enough balance), False otherwise.
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is not enough balance to do something by subtracting the amount from the current balance.
    # It prints the amount for demonstration purposes and returns True if the result is not greater than 0 (i.e., there is not enough balance), False otherwise.
    print(amount)
    return not sub(balance, amount) > 0
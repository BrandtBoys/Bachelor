def mul(a,b):
    # This function calculates the product of two numbers using a simple loop
    return a*b

def falc(a):
    # This function calculates the factorial of a number using multiplication
    res = 1
    while a > 0:
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # This function subtracts two numbers and returns the result
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is enough balance to do something
    # It does this by subtracting the amount from the balance and checking if the result is greater than 0
    return sub(balance, amount) > 0

def not_enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is not enough balance to do something
    # It does this by comparing the amount to the balance (which is printed for debugging purposes)
    print(amount)
    return not sub(balance, amount) > 0
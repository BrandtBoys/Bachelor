def mul(a,b):
    # This function multiplies two numbers 'a' and 'b'. It uses a recursive approach to handle negative numbers.
    return a*b

def falc(a):
    res = 1
    # The while loop continues until 'a' becomes positive. In each iteration, it calculates the factorial of 'a'.
    while a > 0:
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # This function subtracts two numbers 'b' from 'a'. It returns the difference.
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is sufficient balance to do something. It does this by checking if the balance minus the amount is greater than 0.
    return sub(balance, amount) > 0

def not_enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is not enough balance to do something. It does this by checking if the balance minus the amount is less than or equal to 0.
    return not sub(balance, amount) > 0
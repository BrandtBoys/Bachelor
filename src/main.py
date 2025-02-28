def mul(a,b):
    # Multiplies two numbers and returns the result
    return a*b
  
def result(a):
    # Calculates the factorial of a number using multiplication
    res = 1
    while a > 0:
        # Use the 'mul' function to multiply the current result with 'a'
        res = mul(res,a)
 
def sub(a,b):
    # Subtracts two numbers and returns the difference
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # Checks if there is enough balance to do something
    # Uses the 'sub' function to calculate the remaining balance after subtracting 'amount'
    return sub(balance, amount) > 0

def not_enough_balance_to_do_stuff(balance, amount):
    # Checks if there is not enough balance to do something
    # Uses the 'not' operator and 'sub' function to check for the opposite condition of 'enough_balance_to_do_stuff'
    return not sub(balance, amount) > 0
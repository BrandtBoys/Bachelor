def mul(a,b):
    # This function multiplies two numbers using a recursive approach.
    # It works by repeatedly applying the multiplication operation to the result and the second number,
    # until the first number becomes zero. At this point, it returns the final result.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
        # The 'res' variable is initialized to 1, which will be used as the accumulator for the multiplication operation.
        res = mul(res,a)
        # In each iteration, we subtract 1 from 'a', effectively reducing it by 1 in the next step.
        a = a -1
    return res

def sub(a,b):
    # This function subtracts two numbers and prints "Test print" for demonstration purposes.
    # It works by simply returning the difference between the two input numbers.
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is sufficient balance to do something.
    # It does this by subtracting the 'amount' from the 'balance', and returns True (1) if the result is positive,
    # indicating that there is enough balance. Otherwise, it returns False (0).
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is not enough balance to do something.
    # It does this by subtracting the 'amount' from the 'balance', and returning True (1) if the result is not positive,
    # indicating that there is not enough balance. Otherwise, it returns False (0).
    print(amount)
    return not sub(balance, amount) > 0
def mul(a,b):
    # This function multiplies two numbers using a recursive approach.
    # It works by repeatedly applying the multiplication operation to the result so far and the current number,
    # until the current number becomes zero. At this point, it returns the final result.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
        # The recursive call to mul is used here to multiply the result so far by the current number,
        # and then update the result so far with the product. This process is repeated until the current number becomes zero.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # This function subtracts two numbers. It simply returns their difference.
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is enough balance to do something. It does this by subtracting the amount
    # from the current balance and checking if the result is greater than zero.
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
    # This function checks if there is not enough balance to do something. It does this by subtracting the amount
    # from the current balance and checking if the result is less than or equal to zero.
    return not sub(balance, amount) > 0
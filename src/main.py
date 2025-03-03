def mul(a,b):
    # This function multiplies two numbers 'a' and 'b' using a loop
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
        # Multiply the result by 'a' in each iteration, effectively calculating a^a
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # This function subtracts 'b' from 'a' and prints "Test print"
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # Check if the balance is greater than or equal to the required amount
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
     # Print the amount and check if the balance is less than the required amount
    print(amount)
    return not sub(balance, amount) > 0
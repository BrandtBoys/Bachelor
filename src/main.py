def mul(a,b):
    # This function multiplies two numbers together and returns the result.
    return a*b

def calculate(a):
    # This function calculates the factorial of a number using multiplication.
    res = 1
    
    while a > 0:
        # For each iteration, multiply the current result by 'a' and update 'a' to be one less than before.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # This function subtracts two numbers together and prints "Test print" for some reason.
    # The purpose of this line is unclear, but it seems to be a leftover from previous development.
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is enough balance in the account to do something.
    # It does this by subtracting 'amount' from 'balance' and checking if the result is greater than 0.
    return sub(balance, amount) > 0

def not_enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is not enough balance in the account to do something.
    # It does this by subtracting 'amount' from 'balance', printing the result for some reason,
    # and checking if the result is less than or equal to 0.
    print(amount) 
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    # This function buys a pizza if there is enough balance in the account.
    # It does this by subtracting 'price' from 'balance', creating a dictionary for the pizza,
    # and checking if there is enough balance to do so.
    
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
    # If there is enough balance, return the pizza dictionary; otherwise, return None.
    enough = not_enough_balance_to_do_stuff(new_balance, price)
    if enough:
        return pizza
    else:
        return None
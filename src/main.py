def mul(a,b):
    # This function multiplies two numbers together and returns the result.
    return a*b

def calculate(a):
    # This function calculates the factorial of a given number 'a' using multiplication.
    res = 1
    
    while a > 0:
        # For each iteration, multiply the current result by 'a' and update 'a' to be one less than before.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # This function subtracts two numbers together and prints "Test print" for demonstration purposes.
    # In a real-world application, this would likely be replaced with a more robust method of subtraction.
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is sufficient balance to do something (in this case, subtracting 'amount' from 'balance').
    # It returns True if the result of the subtraction is greater than 0, indicating that there is enough balance.
    return sub(balance, amount) > 0

def not_enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is not enough balance to do something (in this case, subtracting 'amount' from 'balance').
    # It returns True if the result of the subtraction is less than or equal to 0, indicating that there is not enough balance.
    print(amount) 
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    # This function simulates buying a pizza with the given price and balance.
    # It first calculates the new balance after subtracting the price from the original balance.
    new_balance = sub(balance, price)
    
    # It then creates a dictionary representing the pizza, including its price, type, and size.
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
    # It checks if there is enough balance to buy the pizza by calling 'not_enough_balance_to_do_stuff'.
    # If there is enough balance, it returns the pizza dictionary; otherwise, it returns None.
    enough = not_enough_balance_to_do_stuff(new_balance, price)
    if enough:
        return pizza
    else:
        return None
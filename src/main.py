def mul(a,b):
    # This function multiplies two numbers together and returns the result.
    return a*b

def calculate(a):
    # This function calculates the factorial of a given number using multiplication.
    res = 1
    
    while a > 0:
        # For each iteration, multiply the current result by 'a' and update 'a' to be one less than before
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # This function subtracts two numbers together and prints "Test print" for demonstration purposes.
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is enough balance to do something by comparing the result of subtraction with 0.
    return sub(balance, amount) > 0

def not_enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is not enough balance to do something by negating the result of comparison.
    print(amount) 
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    # This function simulates buying a pizza by subtracting the price from the balance and checking for sufficiency.
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
    # If there is enough balance to buy the pizza, return its details; otherwise, return None
    enough = not_enough_balance_to_do_stuff(new_balance, price)
    if enough:
        return pizza
    else:
        return None
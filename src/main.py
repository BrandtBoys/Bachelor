def mul(a,b):
    # Multiplies two numbers together
    return a*b

def calculate(a):
    # Calculates the factorial of a number
    res = 1
    while a > 0: 
        # Repeatedly multiplies the result by 'a' to get the factorial
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # Subtracts one number from another
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # Returns True if there's enough balance to do something
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    # Returns True if there's not enough balance to do something
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    # Subtracts the price of a pizza from the balance
    new_balance = sub(balance, price)
    # Creates a dictionary with information about the pizza
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    # Returns True if there's enough balance to buy the pizza
    enough = not_enough_balance_to_do_stuff(new_balance, price)
    if enough:
        return pizza
    else:
        return None
def mul(a,b):
    # Multiplies two numbers using a simple loop
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
        # Continuously multiplies the result by 'a' as long as 'a' is greater than 0
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # Subtracts 'b' from 'a' and prints a test message (not used in this function)
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # Checks if the balance is sufficient to do something by subtracting 'amount' from 'balance'
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    # Checks if there's not enough balance by negating the result of 'enough_balance_to_do_stuff'
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    # Updates the balance to reflect payment
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    # Checks if the updated balance is enough to buy a pizza
    enough = not_enough_balance(new_balance, price)
    if enough:
        return pizza
    else: 
        # If there's not enough balance, returns None
        return None
def mul(a,b):
    # Multiplies two numbers using a simple recursive function
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
        # Uses the multiplication function to multiply the result by 'a' in each iteration
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # Subtracts one number from another and prints a test message
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # Calculates if the balance is enough to do something by subtracting 'amount' from 'balance'
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    # Checks if there's not enough balance by printing 'amount' and returning the opposite of the previous function
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    # Updates the balance to reflect a payment made for a pizza
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    # Checks if there's enough balance to buy the pizza by calling the previous function
    enough = not_enough_balance_to_do_stuff(new_balance, price) 
    if enough:
        return pizza
    else:
        return None
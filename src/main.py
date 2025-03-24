def mul(a,b):
   # Multiplies two numbers together and returns the result
    return a*b

def calculate(a):
   # Calculates the factorial of a number using multiplication
    res = 1
    while a > 0: 
       # Multiply the current result by 'a' to get the next factor
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
   # Subtracts one number from another and returns the difference
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
   # Returns True if the balance is sufficient to do something, False otherwise
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
   # Returns True if the balance is not enough to do something, False otherwise
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
   # Simulates buying a pizza by subtracting its price from the balance
    new_balance = sub(balance, price)
    # Represents a pizza with its price, type, and size
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
   # Checks if there's enough balance to buy the pizza
    enough = not_enough_balance_to_do_stuff(new_balance, price)
    if enough:
        return pizza
    else:
        return None
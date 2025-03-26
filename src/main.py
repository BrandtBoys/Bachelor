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
    
    print("Test print")
   # Subtracts one number from another
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
   # Returns True if there's not enough balance to do something
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
    enough = not_enough_balance(new_balance, price)
    if enough:
        return pizza
    else return None




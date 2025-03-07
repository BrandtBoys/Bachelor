def mul(a,b):
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
#Here we print something
    
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
#Update balance to reflect payment
    
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
    enough = not_enough_balance(new_balance, price)
    if enough:
        return pizza
    else:
        return None




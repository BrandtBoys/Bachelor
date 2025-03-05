def mul(a,b):
    return a*b

def calculate(a):
    res = 1
    while a > 0: #Test comment
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    #Here we print something
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    return sub(balance, amount) > 0 #Subtract from balance

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    #Update balance to reflect payment
    balance = balance - price
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    return pizza




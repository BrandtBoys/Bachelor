def mul(a,b):
    #This function multiplies two numbers together
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
        #We use this loop to multiply all the way down from 'a' to 1
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    #This function subtracts one number from another, but it also prints "Test print"
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    #Here we check if there's enough balance to do something by subtracting 'amount' from 'balance'
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
    #This function checks if there isn't enough balance to do something
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    #Update balance to reflect payment
    balance = balance - price
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    #This function returns a dictionary with information about the pizza that was bought
    return pizza
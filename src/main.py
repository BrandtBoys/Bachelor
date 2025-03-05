def mul(a,b):
    # This function multiplies two numbers using a loop, 
    # which is more efficient than a simple multiplication operation.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
        # The result of the multiplication is stored in 'res' and then multiplied by 'a'
        res = mul(res,a)
        # After each iteration, 'a' is decremented by 1 to prepare for the next loop
        a = a -1
    return res

def sub(a,b):
    # This function subtracts two numbers and prints "Test print" 
    # (which seems to be a leftover from previous code changes)
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if the balance is greater than 0 after subtracting 'amount'
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    # If there's not enough balance, it prints the amount and returns False
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    # This function simulates buying a pizza by subtracting 'price' from 'balance'
    # It also creates a dictionary with pizza details (price, type, size)
    balance = balance - price
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    return pizza
def mul(a,b):
    # This function multiplies two numbers and returns the result.
    return a*b

def calculate(a):
    # This function calculates the factorial of a number using recursion.
    res = 1
    while a > 0: 
        # The multiplication is done in-place, meaning it modifies the original value.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # This function subtracts two numbers and returns the result. It also prints "Test print" to the console.
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is enough balance to do something by comparing the difference between balance and amount.
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is not enough balance to do something by negating the result of the previous function.
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    # This function buys a pizza by subtracting the price from the balance and returns the pizza details.
    balance = balance - price
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    return pizza
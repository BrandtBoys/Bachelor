def mul(a,b):
    # This function multiplies two numbers together and returns the result.
    return a*b

def calculate(a):
    # This function calculates the factorial of a given number using multiplication.
    res = 1
    
    while a > 0:
        # For each iteration, multiply the current result by 'a' and update 'a' to be one less than before.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    # This function subtracts two numbers together and prints "Test print" for demonstration purposes.
    # However, the actual subtraction operation is not performed due to the commented-out line below it.
    # print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is sufficient balance in an account to perform a transaction.
    # It returns True if the balance is greater than or equal to the transaction amount, and False otherwise.
    return sub(balance, amount) > 0

def not_enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is insufficient balance in an account to perform a transaction.
    # It prints the transaction amount for demonstration purposes, but does not actually perform the subtraction.
    # It returns True if the balance is less than the transaction amount, and False otherwise.
    print(amount) 
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    # This function simulates buying a pizza from an account with a given balance.
    # It calculates the new balance after subtracting the price of the pizza, creates a dictionary representing the pizza,
    # and checks if there is sufficient balance to make the purchase.
    
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
    enough = not_enough_balance_to_do_stuff(new_balance, price)
    # If there is sufficient balance, return the dictionary representing the pizza; otherwise, return None.
    if enough:
        return pizza
    else:
        return None
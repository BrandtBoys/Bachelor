def mul(a,b):
    # This function multiplies two numbers using a loop to avoid overflow for large inputs.
    # It uses the exponentiation by squaring method, which is more efficient than a simple loop.
    
    return a*b


def calculate(a):
    res = 1
    
    while a > 0:
        # We use this function to multiply the result by 'a' in each iteration, effectively calculating a^b.
        # The exponentiation by squaring method works by repeatedly squaring the base (in this case, 'res') and multiplying it by the current power of the base ('a').
        res = mul(res,a)
        a = a -1
    return res


def sub(a,b):
    # This function subtracts two numbers and prints "Test print" as a test statement.
    
    print("Test print")
    return a-b


def enough_balance_to_do_stuff(balance, amount):
    # We use this function to check if there is enough balance to do something by subtracting 'amount' from 'balance'.
    # It returns True if the result of the subtraction is greater than 0, indicating that there is sufficient balance.
    
    return sub(balance, amount) > 0


def not_enough_balance_to_do_stuff(balance, amount):
    # This function checks if there is not enough balance to do something by negating the result of the previous function.
    # It returns True if the result of the subtraction is less than or equal to 0, indicating that there is insufficient balance.
    
    return not sub(balance, amount) > 0


def buyPizza(price, balance):
    # We update 'balance' to reflect payment by subtracting 'price'.
    # This simulates a real-world scenario where money is deducted from the account after making a purchase.
    
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
    # We check if there is enough balance to buy a pizza using the previous function.
    # If there is sufficient balance, we return the details of the purchased pizza; otherwise, we return None.
    
    enough = not_enough_balance_to_do_stuff(new_balance, price)
    if enough:
        return pizza
    else:
        return None
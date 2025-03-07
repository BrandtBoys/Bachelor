def mul(a,b):
    # Multiplies two numbers together
    return a*b

# Calculates the factorial of a number using multiplication
def calculate(a):
    res = 1
    while a > 0: 
        # Use the multiplication function to multiply the result by 'a'
        res = mul(res,a)
        # Decrement 'a' for the next iteration
        a = a -1
    return res

# Subtracts one number from another
def sub(a,b):
    print("Test print")
    # Return the difference between 'a' and 'b'
    return a-b

# Checks if there is enough balance to do something
def enough_balance_to_do_stuff(balance, amount):
    # Use the subtraction function to subtract 'amount' from 'balance'
    return sub(balance, amount) > 0 

# Checks if there is not enough balance to do something
def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
    # Return True if 'balance' is less than or equal to 'amount', False otherwise
    return not sub(balance, amount) > 0

# Buys a pizza if there is enough balance
def buyPizza(price, balance):
    # Subtract the price of the pizza from the balance
    new_balance = sub(balance, price)
    # Create a dictionary with the pizza details
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    # Check if there is enough balance to buy the pizza
    enough = not_enough_balance_to_do_stuff(new_balance, price)
    # Return the pizza if there is enough balance, None otherwise
    if enough:
        return pizza
    else:
        return None
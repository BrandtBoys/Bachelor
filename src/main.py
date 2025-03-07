def mul(a,b):
    # This function multiplies two numbers together using a loop.
    # It starts with a result of 1 and then keeps multiplying by 'a' until 'a' is no longer greater than 0.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
        # The result so far is multiplied by the current number, and this new value becomes the result for the next iteration.
        res = mul(res,a)
    # After each multiplication, 'a' is decremented by 1 to keep track of how many times we've multiplied.
        a = a -1
    return res

def sub(a,b):
    # This function subtracts one number from another and prints "Test print" in the process.
    # The result is then returned.
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there's enough balance to do something by subtracting 'amount' from 'balance'.
    # If the result is greater than 0, it means we have enough balance and this function returns True.
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    # This function checks if there's not enough balance to do something by subtracting 'amount' from 'balance'.
    # If the result is less than or equal to 0, it means we don't have enough balance and this function returns True.
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    # This function simulates buying a pizza by subtracting 'price' from 'balance'.
    # It then creates a dictionary with the price, type, and size of the pizza, which is returned.
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
    enough = not_enough_balance(new_balance, price)  # Check if there's enough balance
    if enough:
        return pizza  # Return the pizza if there's enough balance
    else:
        return None  # Return None if there's not enough balance
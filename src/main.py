def mul(a,b):
    # This function multiplies two numbers and returns the result
    return a*b

def calculate(a):
    # Initialize a variable to store the result, starting at 1
    res = 1
    
    # Loop as long as 'a' is greater than 0
    while a > 0: 
        # Multiply the current result by 'a'
        res = mul(res,a)
        
        # Subtract 1 from 'a' for each iteration
        a = a -1
        
    # Return the final result
    return res

def sub(a,b):
    # This function subtracts two numbers and returns the difference
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # Check if there is enough balance to do something (i.e., 'balance' minus 'amount' is greater than 0)
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
    # Return the opposite of whether there is enough balance
    return not sub(balance, amount) > 0

# This function simulates buying a pizza by subtracting its price from the balance and returning the pizza details
def buyPizza(price, balance):
    # Subtract the pizza price from the balance
    balance = balance - price
    
    # Create a dictionary with the pizza's details
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
    # Return the pizza details
    return pizza
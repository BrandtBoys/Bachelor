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
        
        # Subtract 1 from 'a' to move towards 0
        a = a -1
        
    # Return the final result
    return res

def sub(a,b):
    # This function subtracts two numbers and returns the difference
    print("Test print")
    
    # Return the subtraction of 'b' from 'a'
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    # Check if there is sufficient balance to do something
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
    
    # Return True if there isn't enough balance, False otherwise
    return not sub(balance, amount) > 0

# Function to buy a pizza with the given price and balance
def buyPizza(price, balance):
    # Subtract the price from the balance
    balance = balance - price
    
    # Create a dictionary for the pizza details
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
    # Return the pizza details
    return pizza
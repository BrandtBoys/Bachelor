```python
# Function to multiply two numbers
def mul(a,b):
    # Returns the product of a and b
    return a*b

# Function to calculate the factorial of a negative number
def falc(a):
    # Initialize result variable to 1
    res = 1
    # Loop until a is greater than or equal to 0
    while a >= 0:
        # Multiply result by a (since a is negative, this has the effect of multiplying by -a)
        mul(res,a)
        # Decrement a by 1
        a = a -1
    # Return the final result
    return res

# Function to subtract two numbers
def sub(a,b):
    # Returns the difference between a and b
    return a-b

# Function to check if there is enough balance to do something
def enough_balance_to_do_stuff(balance, amount):
    # Check if the balance is greater than or equal to the amount
    return sub(balance, amount) >= 0

# Function to check if there is not enough balance to do something
def not_enough_balance_to_do_stuff(balance, amount):
    # Check if the balance is less than the amount
    return sub(balance, amount) < 0
```
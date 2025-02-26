```python
# Function to check if there is enough balance to do something
def enough_balance_to_do_stuff(balance, amount):
    # Subtract the amount from the balance and return True if the result is positive (i.e., we have enough)
    return sub(balance, amount) > 0

# Function to check if there is not enough balance to do something
def not_enough_balance_to_do_stuff(balance, amount):
    # Print the current balance for debugging purposes
    print(balance)
    # Return True if the balance after subtracting the amount is not positive (i.e., we don't have enough)
    return not sub(balance, amount) > 0

# Function to multiply two numbers
def mul(a,b):
    # Return the product of a and b
    return a*b

# Function to calculate the factorial of a number
def falc(a):
    # Initialize the result to 1
    res = 1
    # While the input number is greater than 0, multiply the result by the current number and decrement the number
    while a > 0:
        # Use the mul function to calculate the product of the result and the current number
        res = mul(res,a)
        # Decrement the current number
        a = a -1
    # Return the final result
    return res

# Function to subtract two numbers
def sub(a,b):
    # Return the difference between a and b
    return a-b
```
def mul(a,b):
  # This function multiplies two numbers together using recursion.
    # The base case for the recursion is when one of the inputs is zero, in which case the result is also zero.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
      # The result of each multiplication is stored in 'res' and then 'a' is decremented by 1.
        # This loop continues until all factors have been multiplied together, resulting in the final product.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
  # This function subtracts two numbers together. It also includes a print statement for demonstration purposes.
    # The result of the subtraction is returned directly, without any additional processing or checks.
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is enough balance to do something by subtracting the amount from the balance and checking if the result is greater than 0.
    # The comparison operator '>' is used here because it will return True as soon as the balance becomes negative or zero.
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
  # This function returns True if there isn't enough balance to do something and False otherwise.
    # The 'not' keyword is used here because it will return the opposite of the result from the previous function.
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
  # This function simulates buying a pizza by subtracting the price from the balance. It also checks if there is enough balance to make the purchase.
    # The new balance after the purchase is calculated using the 'sub' function.
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
  # If there is enough balance, the function returns the pizza details. Otherwise, it returns None.
    # The 'enough' variable is used here to simplify the logic and make it easier to read.
    enough = not_enough_balance(new_balance, price)
    if enough:
        return pizza
    else:
        return None
def mul(a,b):
  # This function multiplies two numbers and returns the result.
    
    return a*b


def calculate(a):
  # This function calculates the factorial of a number using multiplication.
    res = 1
    
    while a > 0:
      # Multiply the current result by 'a' to get the next factorial value
        res = mul(res,a)
      # Decrement 'a' for the next iteration
        a = a -1
    return res

def sub(a,b):
  # This function subtracts two numbers and returns the difference.
    
    print("Test print")
  # Subtract 'b' from 'a' and return the result
    return a-b


def enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is enough balance to do something (in this case, buying pizza).
    return sub(balance, amount) > 0


def not_enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is not enough balance to do something.
    print(amount) 
  # Return True if the balance is less than or equal to zero, False otherwise
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
  # This function buys a pizza if there is enough balance.
    
    new_balance = sub(balance, price)
  # Create a dictionary with pizza details
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
  # Check if there is enough balance to buy the pizza
    enough = not_enough_balance_to_do_stuff(new_balance, price)
  # If there is enough balance, return the pizza details
    if enough:
        return pizza
  # Otherwise, return None
    else:
        return None




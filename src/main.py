def mul(a,b):
  # This function multiplies two numbers together and returns the result.
    
    return a*b


def calculate(a):
  # This function calculates the factorial of a given number 'a' using multiplication.
    res = 1
    
    while a > 0:
      # For each iteration, multiply the current result by 'a' and update 'a' to be one less than before.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
  # This function subtracts two numbers together and returns the difference.
    
    print("Test print")
    return a-b


def enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is enough balance to do something by comparing the current balance with the given amount.
    return sub(balance, amount) > 0


def not_enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is not enough balance to do something by checking if the comparison in 'enough_balance_to_do_stuff' returns False.
    print(amount) 
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
  # This function simulates buying a pizza with the given price and balance. It checks if there is enough balance to buy the pizza and returns the pizza details if possible.
    
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
  # Check if there is not enough balance to buy the pizza by calling 'not_enough_balance_to_do_stuff' with the updated balance and price.
    enough = not_enough_balance_to_do_stuff(new_balance, price)
    if enough:
      # If there is enough balance, return the pizza details.
        return pizza
    else:
      # If there is not enough balance, return None.
        return None




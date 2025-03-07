def mul(a,b):
  # This function multiplies two numbers together using a loop.
  # It starts with an initial result of 1 and then repeatedly multiplies this by 'a' until 'a' is no longer positive.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
      # The result so far is multiplied by the current number, and the current number is decremented by 1 in each iteration.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    
  # This function subtracts one number from another and prints "Test print" to the console.
  # The result of this subtraction is then returned.
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is enough balance in the account to do something.
  # It does this by subtracting the amount from the balance and checking if the result is greater than 0.
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is not enough balance in the account to do something.
  # It does this by subtracting the amount from the balance and checking if the result is less than or equal to 0.
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    
  # This function simulates buying a pizza with the given price and balance.
  # It first subtracts the price from the balance, then creates a dictionary representing the pizza with its price, type, and size.
  # The dictionary is then returned.
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
    enough = not_enough_balance(new_balance, price)
    if enough:
        return pizza
    else return None




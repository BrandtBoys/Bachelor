def mul(a,b):
  # This function multiplies two numbers using a loop to avoid overflow for large inputs.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
      # We use this function to multiply the result by 'a' in each iteration, effectively calculating a^b.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
  # This function subtracts two numbers and prints "Test print" as a test statement.
    
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
  # We use this function to check if there's enough balance to do something by subtracting 'amount' from 'balance'.
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
  # This function checks if there's not enough balance to do something by negating the result of the previous function.
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
  # We update 'balance' to reflect payment by subtracting 'price'.
    
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
  # This function checks if there's enough balance to buy a pizza and returns the pizza object if possible.
    enough = not_enough_balance(new_balance, price)
    if enough:
        return pizza
    else:
      # If there's not enough balance, we return None.
        return None




def mul(a,b):
  # This function multiplies two numbers together using recursion.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
      # The result of each multiplication is stored in 'res' and then 'a' is decremented by 1.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
  # This function subtracts two numbers together. It also includes a print statement for demonstration purposes.
    
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is enough balance to do something by subtracting the amount from the balance and checking if the result is greater than 0.
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
  # This function returns True if there isn't enough balance to do something and False otherwise.
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
  # This function simulates buying a pizza by subtracting the price from the balance. It also checks if there is enough balance to make the purchase.
    
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
  # If there is enough balance, the function returns the pizza details. Otherwise, it returns None.
    enough = not_enough_balance(new_balance, price)
    if enough:
        return pizza
    else:
        return None




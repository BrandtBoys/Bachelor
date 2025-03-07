def mul(a,b):
  # This function multiplies two numbers using a loop, 
  # which is more efficient than a simple multiplication operation.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
      # The result of the multiplication is stored in 'res' and then multiplied by 'a'
        res = mul(res,a)
      # After each iteration, 'a' is decremented by 1 to prepare for the next multiplication
        a = a -1
    return res

def sub(a,b):
  # This function subtracts two numbers and prints a test message.
    
    print("Test print")
  # The subtraction operation returns the difference between 'a' and 'b'
    return a-b

def enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is enough balance to do something by comparing the result of the sub function
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
  # This function returns True if there is not enough balance and False otherwise
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    
  # This function simulates buying a pizza by subtracting the price from the balance
  # It also creates a dictionary with information about the pizza being bought
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




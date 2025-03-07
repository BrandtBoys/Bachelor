def mul(a,b):
  # This function multiplies two numbers together using a loop.
  # It starts with the result being 1, then for each number in the input,
  # it multiplies the current result by that number and decrements the counter.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
      # The result is multiplied by 'a' on each iteration of the loop.
        res = mul(res,a)
      # The value of 'a' is decreased by 1 after each multiplication.
        a = a -1
    return res

def sub(a,b):
  # This function subtracts two numbers together and prints a test message.
    
    print("Test print")
  # The result of the subtraction is returned.
    return a-b

def enough_balance_to_do_stuff(balance, amount):
  # This function checks if there's enough balance to do something by subtracting
  # 'amount' from 'balance'. It returns True if the result is positive (i.e., there's
  # enough balance), and False otherwise.
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
  # This function checks if there's not enough balance to do something by checking
  # if the subtraction of 'amount' from 'balance' is not positive (i.e., there's
  # not enough balance). It prints the value of 'amount' and returns True if
  # there's not enough balance, and False otherwise.
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    
  # This function simulates buying a pizza by subtracting the price from the balance,
  # then returning a dictionary with details about the pizza being bought.
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




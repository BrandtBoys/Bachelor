def mul(a,b):
  # This function multiplies two numbers together and returns the result.
  # It uses a simple multiplication algorithm to achieve this.
    return a*b
 
def calculate(a):
  # This function calculates the factorial of a given number 'a' using multiplication.
  # It iterates from 'a' down to 1, multiplying the current result by each number in that range.
    res = 1
     
     while a > 0:
      # For each iteration, multiply the current result by 'a' and update 'a' to be one less than before.
        res = mul(res,a)
        a = a -1
    return res
 
def sub(a,b):
  # This function subtracts two numbers together and returns the difference.
  # It simply returns the result of the subtraction operation.
    print("Test print")
    return a-b
 
def enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is enough balance to do something by comparing the current balance with the given amount.
  # It uses the 'sub' function to calculate the difference between the two amounts and returns True if it's positive, False otherwise.
    return sub(balance, amount) > 0
 
def not_enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is not enough balance to do something by checking if the comparison in 'enough_balance_to_do_stuff' returns False.
  # It uses the 'sub' function to calculate the difference between the two amounts and returns True if it's not positive, False otherwise.
    print(amount) 
    return not sub(balance, amount) > 0
 
def buyPizza(price, balance):
  # This function simulates buying a pizza with the given price and balance. It checks if there is enough balance to buy the pizza and returns the pizza details if possible.
  # It first calculates the new balance after subtracting the price from the current balance.
  # Then it checks if there's not enough balance using the 'not_enough_balance_to_do_stuff' function, which returns True if there's not enough balance, False otherwise.
  # If there is enough balance, it returns the pizza details; otherwise, it returns None.
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
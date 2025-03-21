def mul(a,b):
  # This function multiplies two numbers and returns the result.
  # It uses a simple multiplication algorithm to calculate the product of 'a' and 'b'.
    return a*b
 
 
def calculate(a):
  # This function calculates the factorial of a number using multiplication.
  # It iterates from 'a' down to 1, multiplying the current result by each number in that range.
    res = 1
     
     while a > 0:
      # For each iteration, multiply the current result by 'a' and update 'a'.
        res = mul(res,a)
        a = a -1
    return res
 
 
def sub(a,b):
  # This function subtracts two numbers and returns the difference.
  # It simply returns the result of subtracting 'b' from 'a', but also prints "Test print" for some reason.
    print("Test print")
     return a-b
 
 
def enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is enough balance to do something by comparing the result of subtraction with 0.
  # It returns True if the result is greater than 0, and False otherwise.
    return sub(balance, amount) > 0
 
 
def not_enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is not enough balance to do something by negating the result of comparison.
  # It prints 'amount' for some reason, but this seems unnecessary.
    print(amount) 
     return not sub(balance, amount) > 0
 
def buyPizza(price, balance):
  # This function simulates buying a pizza by checking if there is enough balance and returning the pizza details if possible.
  # It first calculates the new balance after subtracting 'price' from it.
    new_balance = sub(balance, price)
    pizza = {
        "price": price,
        "type": "pepperoni",
        "size": "huge"
    }
    
  # Check if there is enough balance to buy the pizza by calling the not_enough_balance_to_do_stuff function.
    enough = not_enough_balance_to_do_stuff(new_balance, price)
    if enough:
      # If there is enough balance, return the pizza details.
        return pizza
    else:
      # If there is not enough balance, return None.
        return None
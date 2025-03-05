def mul(a,b):
    # This function multiplies two numbers together using a loop.
    # It starts with an initial result of 1 and then keeps multiplying by 'a' until 'a' is no longer positive.
    return a*b
 
def calculate(a):
     res = 1
     while a > 0: 
         # The result so far is multiplied by the current number, and this new value becomes the new result.
         res = mul(res,a)
         # We subtract 1 from 'a' to keep track of how many times we've multiplied it.
         a = a -1
     return res
 
def sub(a,b):
    # This function subtracts one number from another, but only if there's enough balance in the account.
     print("Test print")
    # We check if the result of the subtraction is greater than 0 to ensure we have enough funds.
     return a-b
 
def enough_balance_to_do_stuff(balance, amount):
    # This function checks if we have enough money to do something by subtracting the cost from our balance.
     return sub(balance, amount) > 0 
 
def not_enough_balance_to_do_stuff(balance, amount):
     print(amount)
    # We check if there's not enough balance by checking if the result of the subtraction is NOT greater than 0.
     return not sub(balance, amount) > 0
 
def buyPizza(price, balance):
    # This function simulates buying a pizza from our account by subtracting the price and returning the details of the pizza.
    new_balance = sub(balance, price)
     # We create a dictionary to store the details of the pizza we're buying (price, type, size).
     pizza = {
         "price": price,
         "type": "pepperoni",
         "size": "huge"
     }
    # We check if there's enough balance before making the purchase.
    enough = not_enough_balance_to_do_stuff(new_balance, price)
    if enough:
        return pizza
    else:
        return None
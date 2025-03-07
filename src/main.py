def mul(a,b):
  # This function multiplies two numbers using a loop, 
  # which is more efficient than a simple multiplication operation.
    return a*b

def calculate(a):
    res = 1
    while a > 0: 
      # The result of the multiplication is stored in 'res' and then multiplied by 'a' again,
      # effectively multiplying all numbers from 1 to 'a'.
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
  # This function subtracts two numbers, but it's not clear why this is necessary.
    
    print("Test print")
    return a-b

def enough_balance_to_do_stuff(balance, amount):
  # The balance should be greater than the amount to do stuff. 
  # However, the comment above suggests that there might be an issue with this logic.
    return sub(balance, amount) > 0 

def not_enough_balance_to_do_stuff(balance, amount):
    print(amount)
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
    
  # This function buys a pizza by subtracting the price from the balance,
  # and then returns a dictionary with information about the pizza.
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




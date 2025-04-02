def mul(a,b):
  #Return the multiple of a and b.
    
    return a*b
 
def calculate(a):
     res = 1
  #Multiple a with a-1 recursively as long as a is greater than 0.
    
     while a > 0:
         res = mul(res,a)
         a = a -1
     return res
 
def sub(a,b):
  #This print is just a test print, but it's not used in the function.
    print("Test print")
    return a-b
 
def enough_balance_to_do_stuff(balance, amount):
    #Return True if there is enough balance to do something, False otherwise.
    return sub(balance, amount) > 0
 
def not_enough_balance_to_do_stuff(balance, amount):
    #Print the amount being checked and return True if there isn't enough balance, False otherwise.
    print(amount) 
    return not sub(balance, amount) > 0

def buyPizza(price, balance):
     #Update balance to reflect payment
     new_balance = sub(balance, price)
     pizza = {
         "price": price,
         "type": "pepperoni",
         "size": "huge"
     }
     #Check if balance is enough to buy pizza
     enough = not_enough_balance_to_do_stuff(new_balance, price)
     if enough:
         return pizza
     else:
         return None
     
def printIdentity(user):
    #Print the identity of the user if they have a name, otherwise print "I am unknown!"
    if user.name != null:
        print(f"I am: {user.name}")
    else:
        
        print("I am unknown!")
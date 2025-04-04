# Returns the product of two numbers.def mul(a,b):
#Return the multiple of a and b.
    
    return a*b


# Calculate the factorial of a given number 'a' by multiplying all numbers from 'a' down to 1.def calculate(a):
    res = 1
#Multiple a with a-1 recursively as long as a is greater than 0.
    
    while a > 0:
        res = mul(res,a)
        a = a -1
    return res

# This function takes two arguments, 'a' and 'b', and returns their difference.def sub(a,b):
#This print is just a test print
    
    print("Test print")
    return a-b


def enough_balance_to_do_stuff(balance, amount):
    return sub(balance, amount) > 0


# Checks if there is enough balance to perform an action, returning True if sufficient funds are available.def not_enough_balance_to_do_stuff(balance, amount):
    print(amount) 
    return not sub(balance, amount) > 0

# Update user's balance after making a purchase and return a dictionary containing details of the purchased pizza.def buyPizza(price, balance):
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
    if user.name != null:
        print(f"I am: {user.name}")
    else:
        
        print("I am unknown!")





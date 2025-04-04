def mul(a,b):
    #Return the multiple of a and b.
    return a*b

#Calculate the factorial of a
def calculate(a):
    res = 1
    #Multiple a with a-1 recursively as long as a is greater than 0.
    while a > 0:
        res = mul(res,a)
        a = a -1
    return res

def sub(a,b):
    #This print is just a test print
    print("Test print")
    return a-b

#Checks if there is enough balance to do somehting
def enough_balance_to_do_stuff(balance, amount):
    return sub(balance, amount) > 0

#hello
def not_enough_balance_to_do_stuff(balance, amount):
    print(amount) #Hello
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
    
#Prints the identity of the user    
def printIdentity(user):
    if user.name != null:
        print(f"I am: {user.name}")
    else:
        #If user.name is not valid, print information about the user being unknown
        print("I am unknown!")





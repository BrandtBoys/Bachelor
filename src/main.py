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
    # This function subtracts two numbers, but it doesn't handle negative numbers.
    print("Test print")
    return a-b
 
def enough_balance_to_do_stuff(balance, amount):
    # This function checks if there's enough balance to do something by subtracting 'amount' from 'balance'.
     return sub(balance, amount) > 0 
 
def not_enough_balance_to_do_stuff(balance, amount):
     print(amount)
    # This function returns the opposite of the previous one, which is used when there's not enough balance.
     return not sub(balance, amount) > 0
 
def buyPizza(price, balance):
    # This function simulates buying a pizza by subtracting 'price' from 'balance'.
    # It also creates a dictionary with information about the pizza being bought.
    new_balance = sub(balance, price)
     pizza = {
         "price": price,
         "type": "pepperoni",
         "size": "huge"
     }
-    return pizza
+    
+    enough = not_enough_balance_to_do_stuff(new_balance, price)  # Changed to use the new function
+    if enough:
+        return pizza
+    else: 
+        return None  # Added a return statement for when there's not enough balance
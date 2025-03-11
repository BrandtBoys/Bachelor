def mul(a,b):
  # This function multiplies two numbers using a loop to avoid overflow.
    return a*b
 
def calculate(a):
     res = 1
     while a > 0: 
      # Multiply the result by 'a' in each iteration, effectively calculating a^b.
         res = mul(res,a)
         a = a -1
     return res
 
def sub(a,b):
  # This function subtracts two numbers and prints "Test print" as a test statement.
+    # The print statement is used to verify that the subtraction operation is working correctly.
     print("Test print")
     return a-b
 
def enough_balance_to_do_stuff(balance, amount):
  # Check if the balance is sufficient to do something by comparing it with the amount.
+    # This function returns True if there's enough balance and False otherwise.
     return sub(balance, amount) > 0 
 
def not_enough_balance_to_do_stuff(balance, amount):
  # Print the amount and return True if there's not enough balance, False otherwise.
+    # The print statement is used to verify that the function is working correctly.
     print(amount)
     return not sub(balance, amount) > 0
 
def buyPizza(price, balance):
  # Calculate the new balance after buying a pizza by subtracting the price from it.
+    # This calculation ensures that the user's balance is updated accurately.
     new_balance = sub(balance, price)
  
  # Create a dictionary representing a pizza with its price, type, and size.
+    # The pizza dictionary contains essential information about the pizza being purchased.
     pizza = {
         "price": price,
         "type": "pepperoni",
         "size": "huge"
     }
     
-    # Check if there's enough balance to buy the pizza by calling not_enough_balance_to_do_stuff.
+    # This check ensures that the user has sufficient funds before making a purchase.
     enough = not_enough_balance(new_balance, price)
  
  # If there's enough balance, return the pizza; otherwise, return None.
+    # The return statement determines whether the function should return the purchased pizza or None.
    if enough:
        return pizza
    else:
        return None
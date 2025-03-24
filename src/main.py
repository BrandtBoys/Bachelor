def mul(a,b):
     # Multiplies two numbers together
     return a*b
 
-def falc(a):
+def calculate(a):
     # Calculates the factorial of a number
     res = 1
-    while a > 0:
+    while a > 0: 
         # Repeatedly multiplies the result by 'a' to get the factorial
         res = mul(res,a)
         a = a -1
     return res
 
 def sub(a,b):
+    
+    print("Test print")
     # Subtracts one number from another and returns the difference
     return a-b
 
 def enough_balance_to_do_stuff(balance, amount):
-    return sub(balance, amount) > 0
+    return sub(balance, amount) > 0 
 
-#hello
 def not_enough_balance_to_do_stuff(balance, amount):
-    print(amount) #Hello
+    print(amount)
     # Returns True if the balance is not enough to do something, False otherwise
     return not sub(balance, amount) > 0
+
+def buyPizza(price, balance):
+    
+    # Subtracts the price of a pizza from the balance
+    balance = balance - price
+    # Creates a dictionary with information about the pizza
+    pizza = {
+        "price": price,
+        "type": "pepperoni",
+        "size": "huge"
+    }
+    # Returns the pizza details as a dictionary
+    return pizza
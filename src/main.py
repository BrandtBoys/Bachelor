def mul(a,b):
     # Multiplies two numbers together and returns the result
     return a*b
 
-def falc(a):
+def calculate(a):
     # Calculates the factorial of a number using multiplication
     res = 1
-    while a > 0:
+    while a > 0: 
         # Multiply the current result by 'a' to get the next factor
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
+    # Subtract the price from the balance to simulate buying a pizza
+    balance = balance - price
+    # Create a dictionary representing a pizza with its price, type, and size
+    pizza = {
+        "price": price,
+        "type": "pepperoni",
+        "size": "huge"
+    }
+    return pizza
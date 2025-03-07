-   def mul(a,b):
? --
+ def mul(a,b):
-       return a*b
? --
+     return a*b
-   
+ 
-   def calculate(a):
? --
+ def calculate(a):
-       res = 1
? --
+     res = 1
- -     while a > 0: #Test comment
- +     while a > 0: 
? --
+     while a > 0: 
-           res = mul(res,a)
? --
+         res = mul(res,a)
-           a = a -1
? --
+         a = a -1
-       return res
? --
+     return res
-   
+ 
-   def sub(a,b):
? --
+ def sub(a,b):
- -     #Comment
- +     
? --
+     
-       print("Test print")
? --
+     print("Test print")
-       return a-b
? --
+     return a-b
-   
+ 
-   def enough_balance_to_do_stuff(balance, amount):
? --
+ def enough_balance_to_do_stuff(balance, amount):
- -     return sub(balance, amount) > 0 #Test comment
- ?                                     -------------
- +     return sub(balance, amount) > 0 
? --
+     return sub(balance, amount) > 0 
-   
+ 
-   def not_enough_balance_to_do_stuff(balance, amount):
? --
+ def not_enough_balance_to_do_stuff(balance, amount):
-       print(amount)
? --
+     print(amount)
-       return not sub(balance, amount) > 0
? --
+     return not sub(balance, amount) > 0
-   
+ 
- + def buyPizza(price, balance):
? --
+ def buyPizza(price, balance):
- +     
? --
+     
- +     balance = balance - price
+     new_balance = sub(balance, price)
- +     pizza = {
? --
+     pizza = {
- +         "price": price,
? --
+         "price": price,
- +         "type": "pepperoni",
? --
+         "type": "pepperoni",
- +         "size": "huge"
? --
+         "size": "huge"
- +     }
? --
+     }
+     
+     enough = not_enough_balance(new_balance, price)
+     if enough:
- +     return pizza
? ^
+         return pizza
? ^^^
-   
-   
- + 
+     else return None
+ 
+ 
+ 

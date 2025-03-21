def mul(a,b):
  # This function multiplies two numbers and returns the result.
  # It uses a simple multiplication algorithm to achieve this.
    
     return a*b
 
+
 
def calculate(a):
  # This function calculates the factorial of a number using multiplication.
  # It iteratively multiplies the input number 'a' with the current result, 
  # until 'a' becomes zero. The final result is the factorial of 'a'.
     
     res = 1
     
     while a > 0:
      # Multiply the current result by 'a' to get the next factorial value
         res = mul(res,a)
      # Decrement 'a' for the next iteration
         a = a -1
     return res
 
 
def sub(a,b):
  # This function subtracts two numbers and returns the difference.
  # It simply returns the result of the subtraction operation between 'a' and 'b'.
    
     print("Test print")
  # Subtract 'b' from 'a' and return the result
     return a-b
 
+
 
def enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is enough balance to do something (in this case, buying pizza).
  # It uses the subtraction operation to check if the current balance is greater than the amount.
    
     return sub(balance, amount) > 0
 
+
 
def not_enough_balance_to_do_stuff(balance, amount):
  # This function checks if there is not enough balance to do something.
  # It prints the amount and returns True if the balance is less than or equal to zero, False otherwise.
    
     print(amount) 
  # Return True if the balance is less than or equal to zero, False otherwise
     return not sub(balance, amount) > 0
 
def buyPizza(price, balance):
  # This function buys a pizza if there is enough balance.
  # It first calculates the new balance after subtracting the price of the pizza from the current balance.
  # Then it checks if there is enough balance to buy the pizza using the 'enough_balance_to_do_stuff' function.
  # If there is enough balance, it returns a dictionary with the pizza details; otherwise, it returns None.
    
     new_balance = sub(balance, price)
  # Create a dictionary with pizza details
     pizza = {
         "price": price,
         "type": "pepperoni",
         "size": "huge"
     }
     
  # Check if there is enough balance to buy the pizza
     enough = not_enough_balance_to_do_stuff(new_balance, price)
  # If there is enough balance, return the pizza details
     if enough:
         return pizza
  # Otherwise, return None
     else:
         return None
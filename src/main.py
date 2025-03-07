- ZGVmIG11bChhLGIpOgogICAgcmV0dXJuIGEqYgoKZGVmIGNhbGN1bGF0ZShh

- KToKICAgIHJlcyA9IDEKICAgIHdoaWxlIGEgPiAwOiAjVGVzdCBjb21tZW50

- CiAgICAgICAgcmVzID0gbXVsKHJlcyxhKQogICAgICAgIGEgPSBhIC0xCiAg

- ICByZXR1cm4gcmVzCgpkZWYgc3ViKGEsYik6CiAgICAjQ29tbWVudAogICAg

- cHJpbnQoIlRlc3QgcHJpbnQiKQogICAgcmV0dXJuIGEtYgoKZGVmIGVub3Vn

- aF9iYWxhbmNlX3RvX2RvX3N0dWZmKGJhbGFuY2UsIGFtb3VudCk6CiAgICBy

- ZXR1cm4gc3ViKGJhbGFuY2UsIGFtb3VudCkgPiAwICNUZXN0IGNvbW1lbnQK

- CmRlZiBub3RfZW5vdWdoX2JhbGFuY2VfdG9fZG9fc3R1ZmYoYmFsYW5jZSwg

- YW1vdW50KToKICAgIHByaW50KGFtb3VudCkKICAgIHJldHVybiBub3Qgc3Vi

- KGJhbGFuY2UsIGFtb3VudCkgPiAwCgoKCg==

+ def mul(a,b):

+     return a*b

+ 

+ def calculate(a):

+     res = 1

+     while a > 0: 

+         res = mul(res,a)

+         a = a -1

+     return res

+ 

+ def sub(a,b):

+     

+     print("Test print")

+     return a-b

+ 

+ def enough_balance_to_do_stuff(balance, amount):

+     return sub(balance, amount) > 0 

+ 

+ def not_enough_balance_to_do_stuff(balance, amount):

+     print(amount)

+     return not sub(balance, amount) > 0

+ 

+ def buyPizza(price, balance):

+     

+     balance = balance - price

+     pizza = {

+         "price": price,

+         "type": "pepperoni",

+         "size": "huge"

+     }

+     return pizza

+ 

+ 

+ 

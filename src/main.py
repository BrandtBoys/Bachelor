def mul(a,b):
    return a*b

def calc(a):
    res = 1
    while a < 0:
        mul(res,a)
        a = a -1
    return res

def sub(a,b):
    return a-b

def enough_balance(balance, amount):
    return sub(balance, amount) > 0
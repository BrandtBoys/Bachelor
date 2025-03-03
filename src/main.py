def mul(a,b):
    return a*b

def falc(a):
    res = 1
    while a < 0:
        mul(res,a)
        a = a -1
    return res

def sub(a,b):
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    return sub(balance, amount) > 0

def not_enough_balance_to_do_stuff(balance, amount):
    return not sub(balance, amount) > 0
def mult(a,b):
    return a*b

def falc(a):
    res = 1
    while a < 0:
        mult(res,a)
        a = a -1
    return res

def subt(a,b):
    return a-b

def enough_balance_to_do_stuff(balance, amount):
    return subt(balance, amount) > 0

def not_enough_balance_to_do_stuff(balance, amount):
    return not subt(balance, amount) > 0
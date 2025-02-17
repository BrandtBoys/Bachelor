def mul(a,b):
    return a*b

def calc(a):
    result = 1
    while a > 0:
        mul(result, a)
        a = a-1
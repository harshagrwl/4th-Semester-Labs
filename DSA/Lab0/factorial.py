import math

def rec(a):
    if a <= 1:
        return 1
    return a*rec(a-1)

def itr(a):
    fac = 1
    while(a>0):
        fac = fac*a
        a = a-1
    return fac

num = int(input('Enter a number : '))
print(rec(num))
print(itr(num))
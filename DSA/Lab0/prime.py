import math

def isprime(a):
    flag = 0
    for i in range(2,a//2,1):
        if a%i == 0:
            flag = 1
            
    if flag == 1:
        return 1
    else:
        return 0


num = int(input('Enter a number : '))
if(isprime(num)):
    print('False')
else:
    print('True')
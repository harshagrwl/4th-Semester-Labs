import math

def bubble(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if(a[j] > a[j+1]):
                a[j+1],a[j] = a[j],a[j+1]
    return a

def selection(a):
    for i in range(0,len(a)):
        min1 = a[i]
        for j in range(i+1,len(a)):
            min1 = min(min1,a[j])
        if (a[i] > min1):
            a[i],min1 = min1,a[i]
    return a

ip = int(input('Enter the number of elements of the array : '))
arr = [input() for x in range(ip)]
print(bubble(arr))
print(selection(arr))
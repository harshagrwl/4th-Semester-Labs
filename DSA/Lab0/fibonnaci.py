import math

def fib(n):
	a = 0
	b = 1
	if n < 1:
		return
	for i in range(0,n):
		print(b)
		c = a+b
		a = b
		b = c
    
def main():
	num = int(input('Enter a number : '))
	fib(num)

main()
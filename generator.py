t = (m*m for m in range(10))

for x in t:
    print x

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
	a, b = b, a+b
	n=n+1

for x in fib(20):
    print x

# equal f(f(f(x1,x2),x3),x4)

def f(x,y):
    return x*10+y

print reduce(f, [1, 5, 8, 6, 7])

# if bool is TRUE, keep the element, else drop it

def f(x):
    return x % 2 == 1

print filter(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])


def s(n):
    def d(y):
        return n % y == 0
    return filter(d, range(2, n)) == []

print filter(s, range(2,10000))

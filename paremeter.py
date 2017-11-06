def show(a, b, c = 10, *d, **e):
    print "a =", a, "b =", b, "c =", c, "d =", d, "e =", e

show(1, 2)

show(1, 2, 3)

show(1, 2, 3, 'a', 'b')

show(1, 2, 3, 'a', 'b', x = 99, y = 100)

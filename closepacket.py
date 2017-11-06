def ft(*argv):
    def f_sum():
        ax=0
        for i in argv:
            ax = i + i
        return ax
    return f_sum

f = ft(1, 2, 3, 4)

print f

print f()

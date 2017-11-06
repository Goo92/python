# coding=utf-8
# 装饰器： 在代码运行期间动态增加功能的方式


"""
def log(func):
    def wrapper(*args, **kw):
        print 'call %s()：' % func.__name__
        return func(*args, **kw)
    return wrapper
"""


def log(func):
    print 'call %s(): ' % func.__name__
    return func


# 下面的定义相当于 now = log(now)
@log
def now():
    print '2017-11-2'


f = now
f()


# 带参数的decorator
def log_t(text):
    def decorator(func_t):
        print '%s %s(): ' % (text, func_t.__name__)
        return func_t

    return decorator


# 下面的定义相当于 now = log('execute')(now)
@log_t('execute')
def now_t():
    print '2017-11-2'


f_t = now_t
f_t()


# Practise
def log_p(*text):
    if len(text):  # 判断有没有参数
        def decorator_p(func_p):
            def inner():
                print 'Begin %s %s(): ' % (text[0], func_p.__name__)
                func_p()
                print 'End %s' % text[0]
            return inner
        return decorator_p
    else:
        def decorator_p(func_p):
            def inner():
                print 'Begin %s(): ' % func_p.__name__
                func_p()
                print 'End'
            return inner
        return decorator_p


@log_p('call')
def now_p():
    print '2017-11-2'


@log_p()
def now_q():
    print '2017-11-2'


f_p = now_p
f_p()

f_q = now_q
f_q()

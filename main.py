
def doSomething(a, b):
    print(2*a, b + " world")

def func(f,*args):
    f(*args)


func(doSomething,3,"hello")
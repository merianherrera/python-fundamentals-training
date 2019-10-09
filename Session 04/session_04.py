#  Decorators
def stars(func):
    def wrapper(msj):
        print("********")
        func(msj)
        print("********")
    return wrapper

#  Can also be written as hello = stars(hello)
@stars
def hello(msj):
    print(msj)


hello("Hello world")

#  Generators


def my_generator():
    n = 1
    print "this prints first"
    yield n
    n += 1
    print "this prints second"
    yield n


gen = my_generator()
print gen.next()
print gen.next()

# Exceptions


class CustomException(Exception):
    def __init__(self, msj):
        # Python2
        super(CustomException, self).__init__(msj)
        # Python3
        # super().__init__(msj)


def division(x, y):
    if y == 0:
        raise CustomException("Division by zero is not allowed")
    return x / y


division(5, 0)

# Lambda expression

(lambda x: x+1)(2)

# same as

def my_func(x):
    return x+1

my_func(2)




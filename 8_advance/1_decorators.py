# A decorator wraps a function to add extra behaviour without changing the behaviour itself

def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper


@my_decorator
def greet():
    print("hello")


greet()

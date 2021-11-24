def my_decorator(func):
    def wrapper():
        print("Something before function called")
        func()
        print("Something after function callled")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
say_hello()

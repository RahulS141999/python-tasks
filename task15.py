def decorator(msg):
    def inner_decorator(func):
        def wrapper(*args,**kwargs):
            print("decorator msg: ", msg)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return inner_decorator

#@decorator("this is decorator")

def my_function(n):
    return n * 3
#other ways to decleare decorator
my_function = decorator("this is decorator")(my_function)

#call  the func
result = my_function(3)
print("result: ", result)

# decorator

'''
# new function 
def my_decorator(hello):
    def wrapper():
        print("before function")
        hello()
        print("after function")
    return wrapper
@my_decorator
#original function
def hello():
    print("Hello Developers")
hello()
'''
# new function 
def my_deco(func):
    def wrapper():
        result = func()
        return result * 2
    return wrapper

@my_deco
def cal():
    a = 30
    b = 20
    c = a + b
    return c

print(cal())
#convert lower to upper
def to_upper(greet):
    def wrapper():
        result = greet()
        print(result.upper())
    return wrapper
@to_upper
def greet():
    return "hello developer"
print(greet())

# crate the multiplication using decorator
def welcome(login):
    def wrapper():
        print("Please Login Frist")
        login()
        print("Welcome to Dashboard")
    return wrapper
@welcome
def login():
    print("Login Successfully")
login()


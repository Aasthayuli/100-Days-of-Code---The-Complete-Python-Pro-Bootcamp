# Functions are First-class objects, can be passed around as arguments e.g., int/string/float, etc.
import time

from numpy.ma.core import inner


def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

def calculate(calc_function, n1, n2):
    return calc_function( n1, n2)

result = calculate(add, 2,3)
print(result)



# Nested Functions

# def outer_function():
#     print("I'm Outer.")
#
#     def nested_function():
#         print("I'm Inner.")
#
#     nested_function()
#
# outer_function()


# Functions can be returned from other functions

def outer_function():
    print("I'm Outer.")

    def nested_function():
        print("I'm Inner.")

    return nested_function  # no need for paranthesis

# outer_function()

inner_function = outer_function()
inner_function()

## Python Decorator Function

def delayer1(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

def delayer2(function):
    def wrapper_function():
        function()
        function()
    return wrapper_function


@delayer1
def say_hello():
    print("Hello !")


@delayer1
def say_bye():
    print("Bye !")


@delayer2
def say_greeting():
    print("How are you?")


# say_hello() #prints after 2 sec delay
# say_bye() #prints after 2 sec delay
# say_greeting() # prints immediately but 2 times

decorated_function = delayer1(say_greeting)
decorated_function()
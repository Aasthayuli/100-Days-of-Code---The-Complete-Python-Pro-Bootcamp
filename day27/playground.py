# Unlimited positional arguments

# args is a tuple
# def add(*args):
#     _sum = 0
#     for n in args:
#         _sum += n
#     return _sum
#
# print(add(3,5,6,7))
# print(add(3,5,6,7,10,20))
#
#
# def func(*args):
#     # since *args is a tuple we can loop through it.
#     print(args[1])
#
# func(1,2,3,4)



# **kwargs: Many keyword arguments
def calculate(**kwargs):
    # kwargs is a dictionary
    # print(kwargs)
    # print(type(kwargs))

    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)

    print(kwargs["add"])

calculate(add= 3, multiply= 5)

def new_calculation(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


new_calculation(3, add= 3, multiply= 5)

class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make = "Nissan", model= "GT-R")
print(my_car.model)

my_car2 = Car(make = "Nissan2")
print(my_car2.model)
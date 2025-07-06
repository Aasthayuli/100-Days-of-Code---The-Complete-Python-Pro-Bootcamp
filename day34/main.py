#TYPE HINTS

age:int
# age = "twelve"
age = 12 # correct type

def func(num:int) -> bool: # specified that return should be a boolean
    # return num+1  # error coz return should be a boolean
    if num % 2 ==0:
        return True
    return False


print(func(46))
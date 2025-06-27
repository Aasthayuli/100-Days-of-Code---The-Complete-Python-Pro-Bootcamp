import random
# import My_Module

# random_integer=random.randint(1,10)
# print(random_integer)
# print(My_Module.my_favourite_number)



# to get a random floating point no.(excluding 1)
# random_no_from_0_to_1= random.random()
# print(random_no_from_0_to_1)

# to get a number from 1 to 10(excluding 10)
# random_no_from_0_to_10= random.random()*10
# print(random_no_from_0_to_10)

# to get a number from 1 to 100(excluding 100)
# random_no_from_0_to_100= random.random()*100
# print(random_no_from_0_to_100)



# to get a number from 1 to 10(including 10)
# random_float=random.uniform(1,10)
# print(random_float)


random_heads_or_tails=random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
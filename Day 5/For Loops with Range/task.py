# __________________________IMPORTANT_____________________________________________#
print(range(1,10))


#___________________________________________________________________________________________#
#range function with for loop

for number in range(1,11): # excludes 11
    print(number)


for number in range(1,11,3): # jumps 3 steps each time
    print(number)

#________________________________Gauss Challenge____________________________________________________#
total=0
for number in range(1,101):
    total+=number

print(total)
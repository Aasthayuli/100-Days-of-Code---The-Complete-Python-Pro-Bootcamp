programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    123:"Hey I am an Integer."
}

print(programming_dictionary["Bug"])
print(programming_dictionary[123]) # provide key in its actual data type form

# Adding pairs
# programming_dictionary["newKey"] ="Hello! I am the new Key."
# print(programming_dictionary)

# creating empty dictionary
# empty_dictionary ={}

# wipe an existing dictionary
# programming_dictionary={}
# print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
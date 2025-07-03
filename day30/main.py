# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dictionary = {"Key":"Value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
#     a_dictionary ={"key":"value"}# will not reach upto this line
#     print(a_dictionary["non_existent_key"])
# except:
#     print("There was an error.")

# try:
#     file = open("a_file.txt")
#     a_dictionary ={"key":"value"}# will not reach upto this line
#     print(a_dictionary["non_existent_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_msg:
#     print(f"The key {error_msg} doesn't exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")

# try:
#     file = open("a_file.txt")
#     a_dictionary ={"key":"value"}# will not reach upto this line
#     print(a_dictionary["non_existent_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_msg:
#     print(f"The key {error_msg} doesn't exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")

# raising own exception
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

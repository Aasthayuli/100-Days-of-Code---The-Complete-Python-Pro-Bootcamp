# file = open("text.txt")
# contents = file.read()
# print(contents)
# file.close()



# This doesn't require closing the file
# with open("text.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("text.txt", mode="w") as file:
#     file.write("New text.")

# with open("text.txt", mode="a") as file:
#     file.write("\nNew text2- My name is Aastha:)")


# Creates a new file if it doesn't exist.
# with open("text.txt", mode="w") as file:
#     file.write("New text


# Using absolute path for the code to work. I have moved the file to desktop.
with open("A:/Git Init/new_file.txt", mode="w") as file:
    file.write("New text3.\n Appending the new text.")

with open("../newfile.txt", mode="w") as file:
    file.write("New text4.\n Appending the new text.")

with open("../Day 16-100/new_file.txt", mode="w") as file:
    file.write("New text4.\ncreated the new file and added with text.")
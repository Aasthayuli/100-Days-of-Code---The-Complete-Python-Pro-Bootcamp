len("12345")


# to check data type of any variable or type checking
print(type("Hello"))
print(type(123))
print(type(True))
print(type(345.234))

# Type Conversion
print("123"+"456")
print(int("123")+ int("456"))  # typecast to int
# print(int("abc")+ int("456"))  # ValueError: invalid literal for int() as "abc" can't be converted or caste


# print("Number of letters in your name: " + len(input("Enter your name"))) # TypeError
# print(type("Number of letters in your name: " ))
# print(type(len(input("Enter your name: "))))

print("Number of letters in your name: " + str(len(input("Enter your name: ")))) # Typecast to String
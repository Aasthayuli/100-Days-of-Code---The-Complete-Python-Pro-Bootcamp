# def greet():
#     print("hello")
#     print("How do you do?")
#     print("Isn't the weather nice?")
#
# greet()

# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do, {name}?")
greet_with_name("Tanu")

user_input = input("Username: ")
greet_with_name(user_input)
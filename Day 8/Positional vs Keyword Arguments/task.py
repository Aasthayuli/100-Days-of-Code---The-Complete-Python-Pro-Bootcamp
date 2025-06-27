# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")


# Functions with more  than 1 input (Positional Arguments)
def greet_with (name, location):
    print(f"Hello {name}.")
    print(f"what is it like in {location}?")

greet_with("Aastha","Saharsa")
# greet_with("Saharsa", "Aastha")  # nonsense:)

# Keyword Argument
greet_with ( name="Aastha" ,location="Saharsa")
greet_with(location="Saharsa", name="Aastha")  # Now this works!

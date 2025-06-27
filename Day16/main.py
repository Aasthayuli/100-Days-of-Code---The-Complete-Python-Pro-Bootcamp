# import another_module
# print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()
# timmy is the object
# turtle is the module
# Turtle is the class

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)  # prints object's location
# timmy.shape("turtle")
# # timmy.color("green")
# timmy.color("green", "yellow")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)  # canvheight is the attribute in the Screen class
# my_screen.exitonclick()  # the method allows the screen to be running until we click on the screen


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"  # aligns the values(words) with left hand side margin
print(table)

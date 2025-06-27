from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
# tim.color("red")

# draws a straight line
# tim.forward(100)
# tim.right(90)

# draws a square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)



# how to import modules:-
# keyword(from)  module_name  keyword(import)  thing in module
# Example: from turtle import Turtle

# Keyword(import) module_name
# example: import turtle
# then use: tim = turtle.Turtle()

# keyword(from)  module_name  keyword(import)  *
# from turtle import *
# imports everything

# using aliases for import
# Example: import turtle as t
# then use it as: timmy = t.Turtle()


# import heroes, villains
# print(heroes.gen())



# draws a dashed line
# for i in range(20):
#     tim.forward(5)
#     tim.color("white")
#     tim.forward(5)
#     tim.color("black")

# OR

for i in range(15):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

screen = Screen()
screen.exitonclick()
import random
# from turtle import Turtle, Screen
import turtle as t

tim = t.Turtle()

# for i in range(3):
#     tim.forward(100)
#     tim.left(120)
#
# tim.color("yellow")
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# tim.color("blue")
# for i in range(5):
#     tim.forward(100)
#     tim.left(72)
#
# tim.color("green")
# for i in range(6):
#     tim.forward(100)
#     tim.left(60)
#
# tim.color("red")
# for i in range(7):
#     tim.forward(100)
#     tim.left(51.43)
#
# tim.color("orange")
# for i in range(8):
#     tim.forward(100)
#     tim.left(45)
#
# tim.color("pink")
# for i in range(9):
#     tim.forward(100)
#     tim.left(40)

# colors= ["blue", "black", "red", "yellow", "green", "pink", "orange", "DeepSkyBlue"]

# def draw_shape(num_sides, colour):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         tim.color(colour)
#         tim.forward(100)
#         tim.left(angle)

# i = 0
# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n, colors[i])
#     i+=1
#
# distance = [20,25,50]
# angle = [0, 90, 180, 270]
#
# tim.pensize(10)
tim.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcolor = (r,g,b)
    return randomcolor

# def random_walk():
#     # tim.color(random.choice(colors))
#     tim.color(random_color())
#     tim.forward(random.choice(distance))
#     tim.left(random.choice(angle))
#
# for i in range(100):
#     random_walk()



# Drawing a spirograph

def draw_circle():
    tim.color(random_color())
    tim.circle(100)
    tim.right(5)

for i in range(72):
    draw_circle()



screen = t.Screen()
screen.exitonclick()
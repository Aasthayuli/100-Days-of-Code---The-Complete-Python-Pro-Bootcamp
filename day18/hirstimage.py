# import colorgram
# rgb_colors = []
# # Extract 6 colors from image
# colors = colorgram.extract('hirst.jpg', 12)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(233, 234, 226), (233, 239, 233), (156, 54, 77), (13, 107, 147), (208, 157, 92), (201, 167, 31), (231, 204, 112), (216, 232, 236), (141, 81, 70), (126, 170, 187), (236, 216, 224), (195, 146, 167)]

# Setting turtle position initially on the screen
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

# draw a dot
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
















screen = turtle_module.Screen()
screen.exitonclick()

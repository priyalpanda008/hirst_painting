#import colorgram
#rgb_colors = []
#colors = colorgram.extract('image.jpg', 6)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#print(rgb_colors)
#[(245, 243, 237), (248, 241, 244), (238, 240, 246), (201, 164, 112), (239, 246, 241), (152, 75, 50)]#

[(201, 164, 112), (152, 75, 50)]

import turtle as turtle_module
import random
tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
turtle_module.colormode(255)
color_list = [(201, 164, 112), (152, 75, 50)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)


number_of_dots = 101

for dot_count in range(1, number_of_dots ):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)











screen = turtle_module.Screen()
screen.exitonclick()
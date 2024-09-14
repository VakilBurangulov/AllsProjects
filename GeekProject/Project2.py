import turtle
from Project2_def import *

turtle.onkey(forward, 'Up')
turtle.onkey(backward, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.onkey(reset, 'c')
turtle.onkey(red, 'r')
turtle.onkey(green, 'g')
turtle.onkey(blue, 'b')
turtle.onkey(black, 'v')
turtle.onkey(begin, 'q')
turtle.onkey(end, 'e')
turtle.listen()
turtle.mainloop()
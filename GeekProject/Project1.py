import time
from tkinter import *
import turtle
window = Tk()
window.title('Project')
window.geometry('600x600')

canvas = Canvas(window, width=600, height=600)
canvas.pack()

canvas.create_text(50, 200, text='Гуся')
canvas.create_text(50, 300, text='Квадрат')
canvas.create_text(50, 400, text='Треугольник')
canvas.create_text(50, 500, text='Ромб')
canvas.create_text(100, 100, text='Что ты хочешь что бы я нарисовал')
def func(event):

    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    print(images_id)
    if images_id == (1,):

        canvas.delete('all')
        canvas.create_text(100, 200, text='Это окно закроется через три секунды после завершения')
        turtle.left(90)
        turtle.circle(50, 180)
        turtle.color('orange')
        turtle.left(90)
        turtle.begin_fill()
        turtle.forward(5)
        turtle.right(120)
        for _ in range(2):
            turtle.forward(10)
            turtle.right(120)

        turtle.forward(5)
        turtle.end_fill()
        turtle.color('black')

        turtle.penup()
        turtle.right(90)
        turtle.circle(50, 180)
        turtle.pendown()
        turtle.left(180)
        turtle.forward(100)
        turtle.circle(100)
        turtle.circle(100, 180)
        turtle.right(180)
        turtle.circle(50, -180)
        turtle.circle(50, 180)
        turtle.left(180)
        turtle.circle(100, -45)
        turtle.right(135)
        turtle.forward(50)
        turtle.back(50)
        turtle.left(135)
        turtle.circle(100, -90)
        turtle.right(45)
        turtle.forward(50)
        turtle.done
        time.sleep(3)
        turtle.bye()
        window.destroy()
    elif images_id == (2,):

        canvas.delete('all')
        canvas.create_text(100, 200, text='Это окно закроется через три секунды после завершения')
        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)
        time.sleep(3)
        turtle.bye()
        window.destroy()
    elif images_id == (3,):
        canvas.delete('all')
        canvas.create_text(100, 200, text='Это окно закроется через три секунды после завершения')
        for _ in range(3):
            turtle.forward(100)
            turtle.left(120)
        time.sleep(3)
        turtle.bye()
        window.destroy()
    elif images_id == (4,):
        canvas.delete('all')
        canvas.create_text(100, 200, text='Это окно закроется через три секунды после завершения')
        turtle.circle(100, 360, 4)
        time.sleep(3)
        turtle.bye()
        window.destroy()
window.bind('<Button-1>',func)
canvas.mainloop()
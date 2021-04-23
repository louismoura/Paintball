from tkinter import *
from random import *
from math import *


size_window = 700
root = Tk()
root.title('Paint figure')
canvas = Canvas(root, width=size_window, height=size_window, bg="gray")
canvas.pack()


root.title('Paintball')
root.wm_attributes('-topmost', 1)
root.resizable(0, 0)


# Кнопка очистки экрана
def clear_screen():
    canvas.delete('all')


clear_button = Button(text='Clear', command=clear_screen,  font=('Arial', 10, 'bold'))
clear_button.place(x=350, y=60)


def notion(event):
    x, y = event.x, event.y
    print('{} {}'.format(x, y))
    colors = choice(['aquamarine', 'fuchsia', 'aqua', 'blue', 'red', 'green', 'orange',
                     'indigo', 'yellow', 'purple', 'pink', 'lime'])
    figure_size = slider_size.get()
    turn = slider_rotation.get()*pi/180
    canvas.create_polygon(x - (figure_size * sin(60*pi/180 + turn)), y + (figure_size * cos(60*pi/180 + turn)),
                          x - (figure_size * sin(-60*pi/180 + turn)), y + (figure_size * cos(-60*pi/180 + turn)),
                          x - (figure_size * sin(-120*pi/180 + turn)), y + (figure_size * cos(-120*pi/180 + turn)),
                          x - (figure_size * sin(120*pi/180 + turn)), y + (figure_size * cos(120*pi/180 + turn)),
                          fill=colors, outline="black")


canvas = Canvas(root, width=600, height=400, bg="white")
canvas.place(x=50, y=100)
canvas.bind('<Button-1>', notion)


# Ползунок регулирующий размер фигуры
slider_size = Scale(root, from_=100, to_=10, length=200, orient=HORIZONTAL)
slider_size.place(x=250, y=520)
size_label = Label(root, text="Size",  font=('Arial', 10, 'bold'))
size_label.place(x=190, y=540)

# Ползунок регулирующий угол наклона фигуры
slider_rotation = Scale(root, from_=360, to_=0, length=200, orient=HORIZONTAL)
slider_rotation.place(x=250, y=570)
rotation_label = Label(root, text="Rotation", font=('Arial', 10, 'bold'))
rotation_label.place(x=180, y=590)


root.mainloop()

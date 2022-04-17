import turtle
t = turtle
t.speed(0)
turtle.bgcolor('black')
colors = ["orange", "yellow", "orange",  " yellow", "orange"]
sides = 3
distance = 2
angle = 45

for i in range(360):
    t.pencolor(colors[i % sides])
    t.forward(i * distance/sides + i)
    t.left(360/sides + angle)
    t.width(i*sides/360)

t.hideturtle()
turtle.done()



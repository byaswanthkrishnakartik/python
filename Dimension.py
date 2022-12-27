import turtle
w=turtle.Screen()
w.title('spiral Helix')
w.bgcolor('black')
colors=['red','purple','blue','green','orange','yellow']
t=turtle.pen()
t.speed(10)
for x in range(360):
    color=colors[x % len(colors)]
    t.pencolor(color)
    t.width(x /100 +1)
    t.forward(x)
    t.left(59)
turtle.done()
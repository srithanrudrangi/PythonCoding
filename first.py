import turtle
bob = turtle.Pen()
for i in range(4):
    bob.forward(100)
    bob.left(90)
bob.penup()
bob.goto(200, 200)
bob.pendown()
for i in range(2):
    bob.forward(100)
    bob.left(90)
    bob.forward(50)
    bob.left(90)
bob.penup()
bob.goto(-200, -200)
bob.pendown()
for i in range(8):
    bob.forward(100)
    bob.left(216)


turtle.done()

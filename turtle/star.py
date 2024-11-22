import turtle

Win = turtle.Screen()
Win.screensize(400,400)
Win.bgcolor('black')
t = turtle.Turtle()
t.color('gold')
t.width(5)
tr= 3
for i in range(3):
    t.forward(199)
    t.left(360/tr)

t.left(90)
t.penup()
t.forward(120)
t.right(90)
t.pendown()
for i in range(3):
    t.forward(199)
    t.right(360/tr)


turtle.done()
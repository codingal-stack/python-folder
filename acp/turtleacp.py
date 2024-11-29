import turtle

Win = turtle.Screen()
Win.screensize(1920,1920)
Win.bgcolor('black')
t = turtle.Turtle()
t.color('orange')
for i in range(4):
    t.forward(90)
    t.right(90)

turtle.done()
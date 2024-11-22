import turtle
Win = turtle.Screen()
Win.screensize(1920,1920)
Win.bgcolor('black')
t = turtle.Turtle()
t.color('white')
t.right(90)
t.speed(0)
for i in range(350):
    t.forward(10+i)
    t.left(90)
    
turtle.done()
    

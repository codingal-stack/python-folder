import turtle

Win = turtle.Screen()
Win.screensize(400,400)
Win.title('my first turtle program')
Win.bgcolor('lightpink')
t = turtle.Turtle()
t.color('purple')
s = 6
for i in range(s):
    t.forward(100)
    t.right(360/s)



turtle.done()
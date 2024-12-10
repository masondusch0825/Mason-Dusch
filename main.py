import turtle




screen = turtle.Screen()


screen.setup(800, 800)



screen.bgcolor('purple')

t = turtle.Turtle()
t.showturtle()
t2 = turtle.Turtle()
t2.showturtle()
t2.penup()
t3 = turtle.Turtle()
t3.showturtle()
t3.hideturtle()


t.hideturtle()
t2.hideturtle()


t.speed(2000)


t2.penup()
t2.goto(0, 100)

t3.penup()
t3.goto(0, 200)
t.penup()
t.goto(0, 50)
t.pendown()
t.write("All About Me", font=("arial", 30, "bold"), align="center")
t.penup()
t.goto(0, -50)
t.pendown()
t.write("Mason Dusch", font=("arial", 30, "bold"), align="center")
enter = input("press enter to begin")
t.showturtle()
t.clear()
t2.clear()

screen.bgcolor('red')
t.penup()
t.goto(0,200)
t.write("My favorite food", font=("arial", 30, "bold"), align="center")

t.penup()
t.goto(125,0)
t.pendown()
t.fillcolor("cornsilk")
t.begin_fill()
t.setheading(45)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.end_fill()
t.penup()

turtle.addshape("cheeseburger.gif")
t2.shape("cheeseburger.gif")
t2.goto(150,150)
a = t2.stamp()
t.hideturtle()




turtle.addshape("steak.gif")
t2.shape("steak.gif")
t2.goto(0,0)
b = t2.stamp()


turtle.addshape("taco.gif")
t2.shape("taco.gif")
t2.goto(-150,-150)
c = t2.stamp()
t2.goto(0,0)



enter = input("press enter to begin")
t.clear()
t2.clear()
screen.bgcolor('green')
t.penup()
t.goto(0,200)
t.write("My favorite Hobbys", font=("arial", 30, "bold"), align="center")



t.penup()
t.goto(150,-100)
t.pendown()
t.color("HotPink")
t.pencolor("Pink")
t.setheading(0)
t.begin_fill()
t.circle(30)
t.end_fill()

turtle.addshape("Football.gif")
t2.shape("Football.gif")
t2.goto(150,150)
a = t2.stamp()
t.hideturtle()




turtle.addshape("Basketball.gif")
t2.shape("Basketball.gif")
(t2.goto(0,0))
b = t2.stamp()


turtle.addshape("Baseball.gif")
t2.shape("Baseball.gif")
t2.goto(-150,-150)
c = t2.stamp()
t2.goto(0,0)

turtle.addshape("Hockey.gif")
(t2.shape("Hockey.gif"))
t2.goto(-120,-120)
c = t2.stamp()
t2.goto(0,0)


enter = input("press enter to begin")
t.clear()
t2.clear()

t.write("My favorite movies", font=("arial", 30, "bold"), align="center")

t.penup()
t.goto(-225,0)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()



turtle.addshape("Movie1.gif")
t2.shape("Movie1.gif")
t2.goto(150,150)
a = t2.stamp()
t.hideturtle()


turtle.addshape("Movie2.gif")
(t2.shape("Movie2.gif"))
t2.goto(-150,-150)
c = t2.stamp()
t.goto(0,0)

b = (t2.stamp())

enter  = input("Press enter to continue: ")

t2.clear()
screen.bgcolor('orange')

t.clear()
t2.clear()
t.write("My favorite Sports", font=("arial", 30, "bold"), align="center")

t.pendown()
t.goto(-225,0)
t.penup()
t.goto(-50,0)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()
t.penup()









turtle.addshape("Football.gif")
t2.shape("Football.gif")
t2.goto(150,150)
a = t2.stamp()
t.hideturtle()


turtle.addshape("Basketball.gif")
t2.shape("Basketball.gif")
t2.goto(-150,-150)
c = t2.stamp()
t2.goto(0,0)

turtle.done()

import turtle
b = turtle.Turtle()
b.color("pink")
b.write("loading...", align= "right",font=("Calibri", 20, "bold"))
b.screen.bgcolor("black")
b.fillcolor("#C8A2C8")
b.pensize(5)
for i in range (400):
    for f in ("violet", "indigo", "blue","green", "yellow","orange","red"):
        b.color(f)
        b.forward(100)
        b.left(90)


turtle.done()

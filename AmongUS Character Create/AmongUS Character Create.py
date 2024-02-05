import turtle

BODY_COLOR = 'red'
BODY_SHADOW = ''
GLASS_COLOR = '#9acedc'
GLASS_SHADOW = ''

# Initialize the turtle screen
screen = turtle.Screen()

# Create a turtle object
k = turtle.Turtle()

def body():
    k.pensize(20)
    k.fillcolor(BODY_COLOR)
    k.begin_fill()
    # Right Side
    k.right(90)
    k.forward(50)
    k.right(180)
    k.circle(40, -180)
    k.right(180)
    k.forward(200)
    # Head Curve
    k.right(180)
    k.circle(100, -180)
    # Left Side
    k.backward(20)
    k.left(15)
    k.circle(500, -20)
    k.backward(20)
    k.circle(40, -180)
    k.left(7)
    k.backward(50)

    # Hip
    k.up()
    k.left(90)
    k.forward(10)
    k.right(90)
    k.down()
    k.right(240)
    k.circle(50, -70)

    k.end_fill()

def glass():
    k.up()
    k.right(230)
    k.forward(100)
    k.left(90)
    k.forward(20)
    k.right(98)

    k.down()
    k.fillcolor(GLASS_COLOR)
    k.begin_fill()

    k.right(150)
    k.circle(90, -55)

    k.right(180)
    k.forward(1)
    k.right(180)
    k.circle(10, -65)
    k.right(180)
    k.forward(110)
    k.right(180)

    k.circle(50, -190)
    k.right(170)
    k.forward(80)

    k.right(180)
    k.circle(45, -30)

    k.end_fill()

def backpack():
    k.up()
    k.right(60)
    k.forward(100)
    k.right(90)
    k.forward(75)

    k.fillcolor(BODY_COLOR)
    k.begin_fill()

    k.down()
    k.forward(30)
    k.right(255)
    k.circle(300, -30)
    k.right(260)
    k.forward(30)

    k.end_fill()

# Call the functions to draw the ninja
body()
glass()
backpack()

# Exit on click
screen.exitonclick()
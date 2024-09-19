import turtle
import random

t = turtle.Turtle()

t.speed(10)
#t.hideturtle()


screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width = 600, height = 600)
t.clear()



def draw_square(t, length):
    """Draws a square with the given side lengths."""
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_circle(t, radius):
    """Draws a circle with the give radius."""
    t.circle(radius)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360/sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin at the given screen coordinates"""
    #Pumpkin Body
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    #Pumpkin Stem
    t.penup()
    t.goto(x, y+(radius*1.75))
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.end_fill()


def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given coordinates."""
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t,x,y,width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.right(240)
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(240)


def draw_jack_o_lantern(t, x, y, radius, eyeSize,):
    """Draws a Jack-o-lantern on the given coordinates"""
    draw_pumpkin(t,x,y,radius)
    draw_eye(t,x+(radius*.60),y+radius,eyeSize)
    draw_eye(t,x-(radius*.60),y+radius,eyeSize)
    draw_mouth(t, x+(radius//2), y+(radius//2),radius)
    t.penup()
    t.goto(0,0)
    t.pendown()

def draw_star(t,x,y,size):
    """Draws a star of the given size at the given coordinates."""
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_sky(t, num_stars):
    """Draws a starry night sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(25,300)
        size = random.randint(15, 30)
        draw_star(t,x,y,size)



"""draw_square(t,100)

t.clear()

draw_circle(t, 100)

t.clear()

draw_polygon(t, 7, 42)

t.clear()

draw_pumpkin(t,0,-10,50)

t.clear()

draw_jack_o_lantern(t,0,0,100,30)
draw_jack_o_lantern(t,200,0,100,30)

t.clear()

draw_star(t, -100, 150, 30)
draw_star(t, 100, 180, 20)

t.clear()

draw_sky(t,25)

t.clear()"""

draw_jack_o_lantern(t,-150,-250, 100, 30)
draw_jack_o_lantern(t,0,-250,80,25)
draw_jack_o_lantern(t,150,-250,100,30)

draw_sky(t,30)

turtle.exitonclick()
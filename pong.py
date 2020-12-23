import turtle, os
window = turtle.Screen()
window.title("pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)
a_score = 0
b_score = 0
a_paddle = turtle.Turtle()
a_paddle.speed(0)
a_paddle.shape("square")
a_paddle.color("white")
a_paddle.shapesize(stretch_wid=5, stretch_len=1)
a_paddle.penup()
a_paddle.goto(-350, 0)
b_paddle = turtle.Turtle()
b_paddle.speed(0)
b_paddle.shape("square")
b_paddle.color("white")
b_paddle.shapesize(stretch_wid=5, stretch_len=1)
b_paddle.penup()
b_paddle.goto(350, 0)
block = turtle.Turtle()
block.speed(0)
block.shape("square")
block.color("white")
block.penup()
block.goto(0, 0)
block.delta_x = 2
block.delta_y = 2
display = turtle.Turtle()
display.speed(0)
display.shape("square")
display.color("white")
display.penup()
display.hideturtle()
display.goto(0, 260)
display.write("player a: 0  player b: 0", align="center", font=("Courier", 24, "normal"))

def a_paddle_up():
    y = a_paddle.ycor() + 21
    a_paddle.sety(y)
def a_paddle_down():
    y = a_paddle.ycor() - 21
    a_paddle.sety(y)
def b_paddle_up():
    y = b_paddle.ycor() + 21
    b_paddle.sety(y)
def b_paddle_down():
    y = b_paddle.ycor() - 21
    b_paddle.sety(y)
window.listen()
window.onkeypress(a_paddle_up, "e")
window.onkeypress(a_paddle_down, "d")
window.onkeypress(b_paddle_up, "Up")
window.onkeypress(b_paddle_down, "Down")

while True:
    window.update()
    block.setx(block.xcor() + block.delta_x)
    block.sety(block.ycor() + block.delta_y)
    if block.ycor() > 290:
        block.sety(290)
        block.delta_y *= -1
    elif block.ycor() < -290:
        block.sety(-290)
        block.delta_y *= -1
    if block.xcor() > 350:
        a_score += 1
        display.clear()
        display.write("player a: {}  player b: {}".format(a_score, b_score), align="center", font=("Courier", 24, "normal"))
        block.goto(0, 0)
        block.delta_x *= -1
    elif block.xcor() < -350:
        b_score += 1
        display.clear()
        display.write("player a: {}  player b: {}".format(a_score, b_score), align="center", font=("Courier", 24, "normal"))
        block.goto(0, 0)
        block.delta_y *= -1
    if block.xcor() < -340 and block.ycor() < a_paddle.ycor() + 50 and block.ycor() > a_paddle.ycor() - 50:
        block.delta_x *= -1
    elif block.xcor() > 340 and block.ycor() < b_paddle.ycor() + 50 and block.ycor() > b_paddle.ycor() -50:
        block.delta_x *= -1

import turtle
from ball import Ball
from paddle import Paddle


# def difficulty():


def box(vertical, horizental):
    pencil = turtle.Turtle()
    pencil.speed(0)
    pencil.color("white")
    pencil.penup()
    pencil.hideturtle()
    pencil.goto(vertical, horizental)
    return pencil


# input("click")
# box(0, 100).onclick(print("hey!"))


def message(a, b):
    return "Player A: {}  Player B: {}".format(a, b)


def display_window(h, w, bg_color, title):
    win = turtle.Screen()
    win.title("Pong by @{}".format(title))
    win.bgcolor(bg_color)
    win.setup(height=h, width=w)
    return win


window = display_window(600, 800, "blue", "samir")
leftPad = Paddle([-350, 0])
rightPad = Paddle([350, 0])
ball = Ball("square", "red", 4)

counter_a = 0
counter_b = 0

pen = box(0, 260)
pen.write(message(counter_a, counter_b), align="center", font=("Courier", 24, "normal"))


window.listen()
window.onkeypress(leftPad.paddle_down, "s")
window.onkeypress(leftPad.paddle_up, "z")
window.onkeypress(rightPad.paddle_down, "Down")
window.onkeypress(rightPad.paddle_up, "Up")


# main loop
while True:
    window.update()

    # move the ball
    ball.move()

    # checking for borders
    ball.check_borders("y", 290)
    ball.check_borders("y", -290)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -1 * ball.dx
        counter_a += 1
        pen.clear()
        pen.write(message(counter_a, counter_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = -1 * ball.dx
        counter_b += 1
        pen.clear()
        pen.write(message(counter_a, counter_b), align="center", font=("Courier", 24, "normal"))

    # checking for collision
    if ball.xcor() < -330 and (ball.ycor() >= leftPad.ycor() - 50) and (ball.ycor() <= leftPad.ycor() + 50):
        ball.setx(-330)
        ball.dx = -1 * ball.dx
    if ball.xcor() > 330 and (ball.ycor() >= rightPad.ycor() - 50) and (ball.ycor() <= rightPad.ycor() + 50):
        ball.setx(330)
        ball.dx = -1 * ball.dx

    # ball.check_borders("x", 290)
    # ball.check_borders("x", -290)
    # ball.check_borders("y", 390)
    # ball.check_borders("y", -390)

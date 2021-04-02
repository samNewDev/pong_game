import turtle


class Paddle(turtle.Turtle):

    def __init__(self, coordinates):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed(0)
        self.goto(coordinates[0], coordinates[1])

    def paddle_up(self):
        if self.ycor() < 230:
            y = self.ycor()
            y += 20
            self.sety(y)

    def paddle_down(self):
        if self.ycor() > -230:
            y = self.ycor()
            y -= 20
            self.sety(y)

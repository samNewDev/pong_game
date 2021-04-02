import turtle


class Ball(turtle.Turtle):

    def __init__(self, shape, color, difficulty):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape(shape)
        self.color(color)
        self.speed(0)
        self.goto(0, 0)
        self.dx = difficulty
        self.dy = difficulty

    def check_borders(self, axe, coordinate):
        if axe == "y" and (self.ycor() > coordinate if coordinate > 0 else self.ycor() < coordinate):
            self.sety(coordinate)
            self.dy = -1 * self.dy
        elif axe == "x" and (self.xcor() > coordinate if coordinate > 0 else self.xcor() < coordinate):
            self.goto(0, 0)
            self.dx = -1 * self.dx
            # return -1

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

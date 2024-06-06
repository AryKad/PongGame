from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.x_mov = 10
        self.y_mov = 10
        self.spd = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_mov, self.ycor()+ self.y_mov)

    def bounce_y (self):
        self.y_mov *= -1
    def bounce_x (self):
        self.x_mov *= -1
        self.spd *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.spd = 0.1
        self.bounce_x()
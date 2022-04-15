from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """ Making the player model class """

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('black')
        self.setheading(90)
        self.speed('fast')
        self.goto(0, -300)

    def up(self):
        """ Move the paddle up """
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

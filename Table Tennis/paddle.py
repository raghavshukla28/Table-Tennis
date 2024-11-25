from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):               #argument for position to pass cordinates in main class
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)



    def up(self):
        if self.ycor() < 235:
            new_y = self.ycor() + 30
            self.goto(self.xcor(),new_y)
        else:
            pass

    def down(self):
        if self.ycor() > -235:
            new_y = self.ycor() - 30
            self.goto(self.xcor(),new_y)
        else:
            pass





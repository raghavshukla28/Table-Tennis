from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.xmove = 10
        self.ymove = 10


    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)


    def bouncewall(self):
        self.ymove *= -1                #to change the direction of ball after bounce

    def bouncepaddle(self):
        self.xmove *= -1
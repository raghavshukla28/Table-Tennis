from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong 🏓🏓")
screen.tracer(0)

r_paddle = Paddle((365, 0))
l_paddle = Paddle((-370, 0))
t_wall = Paddle((-300, 303))
t_wall.shapesize(stretch_wid=1, stretch_len=150)
t_wall.color("red")
b_wall = Paddle((0, -298))
b_wall.shapesize(stretch_wid=1, stretch_len=150)
b_wall.color("red")
ball = Ball()
scoreboard = Scoreboard()
delay = 0.1

# Movement flags to keep track of whether a paddle should be moving up or down
r_paddle_up = False
r_paddle_down = False
l_paddle_up = False
l_paddle_down = False

# Functions to set the movement flags when keys are pressed
def r_paddle_up_press():
    global r_paddle_up
    r_paddle_up = True

def r_paddle_down_press():
    global r_paddle_down
    r_paddle_down = True

def l_paddle_up_press():
    global l_paddle_up
    l_paddle_up = True

def l_paddle_down_press():
    global l_paddle_down
    l_paddle_down = True

# Functions to reset the movement flags when keys are released
def r_paddle_up_release():
    global r_paddle_up
    r_paddle_up = False

def r_paddle_down_release():
    global r_paddle_down
    r_paddle_down = False

def l_paddle_up_release():
    global l_paddle_up
    l_paddle_up = False

def l_paddle_down_release():
    global l_paddle_down
    l_paddle_down = False

# Function to move the paddles based on the movement flags
def move_paddles():
    if r_paddle_up:
        r_paddle.up()
    if r_paddle_down:
        r_paddle.down()
    if l_paddle_up:
        l_paddle.up()
    if l_paddle_down:
        l_paddle.down()
    # Schedule the move_paddles function to be called again after 20 milliseconds
    screen.ontimer(move_paddles, 20)

# Bind key press events to functions that set movement flags
screen.listen()
screen.onkeypress(r_paddle_up_press, "Up")
screen.onkeypress(r_paddle_down_press, "Down")
screen.onkeypress(l_paddle_up_press, "w")
screen.onkeypress(l_paddle_down_press, "s")

# Bind key release events to functions that reset movement flags
screen.onkeyrelease(r_paddle_up_release, "Up")
screen.onkeyrelease(r_paddle_down_release, "Down")
screen.onkeyrelease(l_paddle_up_release, "w")
screen.onkeyrelease(l_paddle_down_release, "s")

# Start the continuous paddle movement
move_paddles()

is_game_ON = True
while is_game_ON:
    screen.update()
    time.sleep(delay)
    ball.move()

    # Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncewall()

    # Detecting collision with paddle
    if ball.xcor() > 345 and ball.distance(r_paddle) < 50 or ball.xcor() < -347 and ball.distance(l_paddle) < 50:
        ball.bouncepaddle()
        if delay < 0.009:
            delay = delay - 0.00099
        else:
            delay = delay - 0.009

    # Detecting miss with r paddle
    if ball.xcor() > 390:
        ball.clear()
        ball.home()
        ball.bouncepaddle()
        scoreboard.l_point()
        delay = 0.1

    # Detecting miss with l paddle
    if ball.xcor() < -390:
        ball.clear()
        ball.home()
        ball.bouncepaddle()
        scoreboard.r_point()
        delay = 0.1

    # Check if either player has won the game
    if scoreboard.r_score == 10:
        scoreboard.result_r()

    if scoreboard.l_score == 10:
        scoreboard.result_l()

screen.exitonclick()

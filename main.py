from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.onkey(key="w", fun=r_paddle.forward)
screen.onkey(key="s", fun=r_paddle.backward)
screen.onkey(key="Up", fun=l_paddle.forward)
screen.onkey(key="Down", fun=l_paddle.backward)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with  y axis wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with right and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
    # detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()

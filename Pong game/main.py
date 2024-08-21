from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.009)
    screen.update()
    ball.move()

    #detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        #it needs to bounce
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score==10 or scoreboard.r_score == 10:
        game_is_on = False

screen.exitonclick()

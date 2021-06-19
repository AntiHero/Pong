import turtle
import random

WIDTH, HEIGHT = 800, 600

wn = turtle.Screen()
wn.title("Pong by BladeRunner")
wn.bgcolor("black")
wn.setup(width=WIDTH, height=HEIGHT)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .07
ball.dy = .01


def paddle_move(paddle, speed):
    y = paddle.ycor()
    y += speed
    paddle.sety(y)

    # Paddle border interaction
    if paddle.ycor() > 250:
        paddle.sety(250)
    
    if paddle.ycor() < -250:
        paddle.sety(-250)


# Keyboard binding
wn.listen()
wn.onkeypress(lambda: paddle_move(paddle_a, 20), "w")
wn.onkeypress(lambda: paddle_move(paddle_a, -20), "s")
wn.onkeypress(lambda: paddle_move(paddle_b, 20), "Up")
wn.onkeypress(lambda: paddle_move(paddle_b, -20), "Down")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.dy *= -1

    # Ball out of border
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() > 330 and ball.xcor() < 340 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 70):
        ball.dx *= -1

    if ball.xcor() < -330 and ball.xcor() > -340 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 70):
        ball.dx *= -1

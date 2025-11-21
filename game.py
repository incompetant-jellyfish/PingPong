import os
import turtle


wn = turtle.Screen()
wn.title("Ping pong")
wn.bgcolor("black")
wn.setup(width=900, height=700)
wn.tracer(0)

#Score
score_1 = 0
score_2 = 0


# Paddle A
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
#speed of animation, sets the speed to maximum possible speed
paddle_1.shape("square")
paddle_1.color("red")
paddle_1.shapesize(stretch_wid=3, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-450, 0)

# Paddle B
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("blue")
paddle_2.shapesize(stretch_wid=3, stretch_len=1)
paddle_2.penup()
paddle_2.goto(450, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

#pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 290)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Ariel", 22, "bold"))

def paddle_1_up():
    y = paddle_1.ycor()
    y += 35
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 35
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 35
    paddle_2.sety(y)
    
def paddle_2_down():
    y = paddle_2.ycor()
    y -= 35
    paddle_2.sety(y)        

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "x")
wn.onkeypress(paddle_2_up, "o")
wn.onkeypress(paddle_2_down, "n")



  

# Main game loop
while True:
    wn.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #BORDER CHECKING
    if ball.ycor() > 330:
        ball.sety(330)
        ball.dy *= -1 #reverses the direction
        os.system("afplay bounce.wav&")

    elif ball.ycor() < -330:
        ball.sety(-330)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 440:
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -440:
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1


    #Paddle and ball collisons
    if (ball.xcor() > 400 and ball.xcor() < 420) and (ball.ycor() < paddle_2.ycor()+50 and ball.ycor() > paddle_2.ycor() -40):
       ball.dx *= -1
     

    elif (ball.xcor() < -400 and ball.xcor() > -420) and (ball.ycor() < paddle_1.ycor()+50 and ball.ycor() > paddle_1.ycor() -40):
       ball.dx *= -1
       



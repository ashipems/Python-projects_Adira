import turtle
import random
import time

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = ""

text = turtle.Turtle()
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 250)
text.write("Score : 0   |   High Score : 0", align="center", font=("calibri", 24, "bold"))


def goup():
    if head.direction != "down":  
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)
        head.direction = ""
        score = 0
        text.clear()
        text.write("Score : {}   |   High Score : {}".format(score, high_score), align="center", font=("calibri", 24, "bold"))
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        if score > high_score:
            high_score = score
        text.clear()
        text.write("Score : {}   |   High Score : {}".format(score,high_score), align="center", font=("calibri", 24, "bold"))
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            head.goto(0, 0)
            head.direction = ""
            score = 0
            text.clear()
            text.write("Score : {}   |   High Score : {}".format(high_score), align="center", font=("calibri", 24, "bold"))
            for s in segments:
                s.goto(1000, 1000)
            segments.clear()
    time.sleep(0.1)
wn.mainloop()

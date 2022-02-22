#from tkinter import font
import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn . title("snake game")
wn . bgcolor("white")
wn .setup(width=600, height=600)
wn . tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#for segment in segments:
   # segment.goto(1000, 1000)

#segments.clear()


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score = 0 High Score: 0", align="center", font=("Courier", 24, "normal") )




def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def stop():
    head.direction = "stop"






def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        
        head.setx(head.xcor() - 20)

    if head.direction == "right":
     
       head.setx(head.xcor() + 20)


wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(stop,"space")


while True:
    wn.update()

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)


        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape("square")
        new_segments.color("blue")
        new_segments.penup()
        segments.append(new_segments)

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}" .format(score, high_score), align="center", font=("Courier", 24, "normal"))


    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segment:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segment:
             segment.goto(1000, 1000)

            segments.clear()
     

    time.sleep(delay)



wn .mainloop()

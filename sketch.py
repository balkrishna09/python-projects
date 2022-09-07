from turtle import Turtle, Screen

bk = Turtle()
bk.shape("turtle")
screen=Screen()


def move_forwards():
    bk.forward(20)
def move_backward():
    bk.backward(20)
def turn_right():
    new_heading=bk.heading()-10
    bk.setheading(new_heading)
def turn_left():
    new_heading=bk.heading()+10
    bk.setheading(new_heading)
def clear_screen():
    bk.reset()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
import turtle
from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=600,height=500)
user_bet=screen.textinput(title='make your bet ', prompt='which color u want :--> ')
colors=['red','orange','yellow','green','blue','purple']
y_position=[-70,-40,-10,20,50,80]
turtle_list=[]

final_line=Turtle()
final_line.pensize(10)
final_line.penup()
final_line.goto(x=235,y=0)
final_line.forward(10)
final_line.pendown()
final_line.setheading(90)
final_line.forward(200)
final_line.setheading(270)
final_line.forward(400)

for turtle_index in range(0,6):
    bk=Turtle()
    bk.penup()
    bk.shape('turtle')
    bk.color(colors[turtle_index])
    bk.goto(x=-280 , y=y_position[turtle_index])
    turtle_list.append(bk)

if user_bet:
    is_reace_on= True

while is_reace_on:
    for turtle in turtle_list:
        if turtle.xcor()>230:
            is_reace_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f'you won {winning_color} turtle is the winner ')
            else:
                print(f'you lost {winning_color} turtle is the winner')
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()
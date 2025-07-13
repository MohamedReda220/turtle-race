from turtle import Turtle , Screen
import random
window=Screen()
window.title("Momo Turtle Race")
window.setup(600,400)
colors = ["red","blue","green"]
y_postion=[-70,0,70]
turtles=[]
user_bet=window.textinput("make your  bet","guess the winner")
for x in range(3):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-280,y=y_postion[x])
    turtles.append(new_turtle)
def race_start():
    is_race_on=True
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor()>280:
                is_race_on=False
                winning_color=turtle.pencolor()
                display_result(winning_color==user_bet)
            else:
                turtle.forward(random.randint(1,5))    
def display_result(winning_color) :
    result_turtle=Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0,0)
    result_turtle.pendown()
    if winning_color==user_bet:
        window.bgcolor("dark green")
        result_turtle.color("white")
        result_turtle.write("you win ",align="center",font=("arial",28,"normal"))
    else:
        window.bgcolor("medium violet red")
        result_turtle.color("white")
        result_turtle.write("you lose",align="center",font=("arial",28,"normal"))
    race_start()    
race_start()
display_result()
window.exitonclick()
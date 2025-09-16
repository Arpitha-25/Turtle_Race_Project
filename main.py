from turtle import Turtle,Screen
import random
screen=Screen()
is_race_on=False
screen.setup(width=500,height=400)
user_bet=screen.textinput(title='Make your bet',prompt='Which turtle will win the race? Enter a color:(\'red\',\'yellow\',\'blue\',\'green\',\'orange\')')
print('Your guess of color of turtle will win:',user_bet)
colors=['red','yellow','blue','green','orange']
all_turtles=[]
x=-230
y=-150

for each in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(each)
    new_turtle.goto(x, y)
    y+=50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            a=turtle.color()
            is_race_on = False
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

if user_bet==a[0]:
    print(f'You won the bet!!{a[0]} turtle won.')
else:
    print(f'You lost.{a[0]} turtle won.')

screen.exitonclick()

import turtle
import pandas
from turtle import Turtle, Screen
screen=Screen()
screen.title("USA MAP_MATCH")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
state_list=data.state.to_list()
guessed_state=[]
while len(guessed_state)<50:

    input_state = screen.textinput(title=f"{len(guessed_state)}/50 correct", prompt="what's the state name").title()
    if input_state == "Exit":
        break
    if input_state in state_list:
        guessed_state.append(input_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        position=data[data.state == input_state]
        t.goto(int(position.x), int(position.y))
        t.write(input_state)

screen.exitonclick()



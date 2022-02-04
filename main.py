import turtle
from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
state_data = pd.DataFrame(data)
all_states = state_data['state'].tolist()
print(all_states)

guessed_states = []
missed_state = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Game",
                                    prompt="Guess other States!").title()
    if answer_state == 'Exit':
        for state in all_states:
            if state not in guessed_states:
                missed_state.append(state)

        new_to_learn = pd.DataFrame(missed_state)
        new_to_learn.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        coordinate = data[data.state == answer_state]
        t.goto(int(coordinate.x), int(coordinate.y))
        t.write(answer_state)



screen.mainloop()

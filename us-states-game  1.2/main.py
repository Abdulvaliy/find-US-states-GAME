import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
write_states = turtle.Turtle()
write_states.penup()
write_states.hideturtle()


states = pandas.read_csv("50_states.csv")
US_state = states["state"].to_list()

n = 0
correct_guesses = []
states_to_learn = US_state
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{n}/50 States Correct", prompt="What's another state's name?").title()

    # if answer_state == "Exit":
    #     missing_states = []
    #     for state in US_state:
    #         if state not in correct_guesses:
    #             missing_states.append(state)
    #     new_data = pandas.DataFrame(missing_states)
    #     new_data.to_csv("states_to_learn.csvs")
    #     break

    if answer_state == "Exit":
        missing_states = [n for n in US_state if n not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn_2.csv")
        break

    if answer_state in US_state:
        # print(answer_state)
        x_axis = int(states[states.state == answer_state].x)
        y_axis = int(states[states.state == answer_state].y)
        write_states.setposition(x_axis, y_axis)
        write_states.write(f"{answer_state}")
        correct_guesses.append(answer_state)
        n += 1
        # print(correct_guesses)
    else:
        print("Wrong!!!")




# screen.mainloop()

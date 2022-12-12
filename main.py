import random
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import plotly.express as px

# put the numbers from 1 to 49 in a container with checkboxes



with st.form("my_form"):

    # create a list with the checked numbers
    my_list = []
    for i in range (1, 50):
        st.session_state[i] = st.checkbox(f'{i}', value=False)

        if st.session_state[i]:
            my_list.append(i)

    target = st.number_input('Въведете колко числа искате да съвпадат', min_value=1, max_value=6, value=3, step=1)
    submitted = st.form_submit_button("Submit")


if submitted:

    st.write(f'Въведените от Вас числа са: {my_list}')


    winners = []
    counter = 1
    random_list = []

    def winners_func(x, y, z):
        for i in x:
            if i in y:
                if i not in z:
                    z.append(i)
        print(winners)

    container = st.container()

    def rndm_func():
        while len(random_list) < 6:
            rndm = random.choice(range(1, 50))

            if rndm not in random_list:
                random_list.append(rndm)

    # target = 3

    while True:
        rndm_func()
        counter += 1
        winners_func(my_list, random_list, winners)

        if len(winners) < target:

            random_list.clear()
            winners.clear()

        else:
            break

    st.write(f'Имате съвпадение на {target} числа {winners} в тираж номер {counter}: {random_list}.')
    st.write(f'При честота на тиражите веднъж седмично, бяха необходими {int(round(counter/4,0))} седмици (около {int(round(counter/52.177,0))} години), за да се случи съвпадение на {target} числа.')

    # show the code for the app
    # code = python code from this file (main.py)
    code = open('main.py', 'r', encoding="utf8").read()

    with st.expander('Покажи кода на приложението'):
        st.code(code, language='python')

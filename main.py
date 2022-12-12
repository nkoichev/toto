import random
import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import plotly.express as px

# put the numbers from 1 to 49 in a container with checkboxes

st.write('Изберете 6 числа от 1 до 49, за да проверите колко време би отнело, за да бъдат изтеглени.')

with st.form("my_form"):

    # create a list with the checked numbers
    my_list = []
    for i in range (1, 50):
        st.session_state[i] = st.checkbox(f'{i}', value=False)

        if st.session_state[i]:
            my_list.append(i)

    target = st.number_input('Въведете брой на печелившите числа (от 1 до 5). 6-цата е изключена като опция, защото изчисленията биха продължили твърде дълго!', min_value=1, max_value=5, value=5, step=1)
    submitted = st.form_submit_button("Submit")


if submitted:

    st.write(f'Въведените от Вас числа са: {my_list}')


    winners = []
    sedmici = 0
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
        sedmici += 1
        winners_func(my_list, random_list, winners)

        if len(winners) < target:

            random_list.clear()
            winners.clear()

        else:
            break

    st.write(f'Имате съвпадение на {target} числа {winners} в тираж номер {sedmici}: {random_list}.')
    st.write(f'При честота на тиражите веднъж седмично, бяха необходими {int(round(sedmici/52.177*12,0))} месеца (около {int(round(sedmici/52.177,0))} години), за да се случи съвпадение на {target} числа.')

    # show the code for the app
    # code = python code from this file (main.py)
    code = open('main.py', 'r', encoding="utf8").read()

    with st.expander('Покажи кода на приложението'):
        st.code(code, language='python')

    # stop the app from running
    st.stop()
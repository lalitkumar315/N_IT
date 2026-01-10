# wap to generate a number from 1 to 10 and take input a number and match them to find win or loss

import streamlit as st
import random
st.title("Random Number Guessing Game")
user_guess = st.number_input('Enter your guess (1-10)', min_value=1, max_value=10)
if st.button('GUESS'):
    random_number = random.randint(1, 10)
    if user_guess == random_number:
        st.text('Result:')
        st.success(f'Congratulations! You guessed it right. The number was {random_number}. You Win!')
    else:
        st.text('Result:')
        st.error(f'Sorry, you guessed {user_guess}, but the number was {random_number}. You Lose!')
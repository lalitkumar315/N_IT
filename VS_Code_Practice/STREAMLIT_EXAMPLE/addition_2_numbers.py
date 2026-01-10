# Wap to add two numbers using streamlit

import streamlit as st
st.title("Addition App")
num1 = st.number_input('Enter the First Number')
num2 = st.number_input('Enter the Second Number')
if st.button('ADD'):
    st.text('Result:')
    st.success(f'Addition of first number: {int(num1)} and Second Number: {num2} is {num1+num2}')
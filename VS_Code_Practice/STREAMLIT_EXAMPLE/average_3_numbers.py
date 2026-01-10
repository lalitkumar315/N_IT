# wap to ask user for 3 numbers and find avg using streamlit

import streamlit as st
st.title("Average App")
num1 = int(st.number_input('Enter the First Number'))
num2 = int(st.number_input('Enter the Second Number'))
num3 = int(st.number_input('Enter the Third Number'))
if st.button('AVG'):
    average = (num1 + num2 + num3) / 3
    st.text('Result:')
    st.success(f'The average of the numbers {num1}, {num2}, and {num3} is : {int(average)}')
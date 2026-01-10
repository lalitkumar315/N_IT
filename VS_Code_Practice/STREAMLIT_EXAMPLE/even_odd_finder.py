# wap to take a number and find even or odd

import streamlit as st
st.title("Even Odd Finder App")
num = st.number_input('Enter a Number')
if st.button('CHECK'):
    if num % 2 == 0:
        st.text('Result:')
        st.success(f'The number {num} is Even')
    else:
        st.text('Result:')
        st.success(f'The number {num} is Odd')

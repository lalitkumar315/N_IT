# wap to calculate area of triangle using streamlit

import streamlit as st
st.title("Area of Triangle App")
base = int(st.number_input('Enter the Base of Triangle'))
height = int(st.number_input('Enter the Height of Triangle'))
if st.button('SUBMIT'):
    area = 0.5 * base * height
    st.text('Result:')
    st.success(f'The area of the triangle with base {base} and height {height} is : {int(area)}')
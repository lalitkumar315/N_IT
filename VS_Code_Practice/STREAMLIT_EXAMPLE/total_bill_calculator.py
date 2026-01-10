# wap to ask for bill and tip and calculate total bill using streamlit

import streamlit as st
st.title("Total Bill Calculator App")
bill = st.number_input('Enter the Bill Amount')
tip = st.number_input('Enter the Tip Amount')
if st.button('CALCULATE'):
    total = bill + tip
    st.text('Result:')
    st.success(f'The total bill amount including tip is {total}')
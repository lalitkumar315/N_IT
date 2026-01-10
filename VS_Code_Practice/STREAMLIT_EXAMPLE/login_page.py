# Assignment-2: How to Create login page using Streamlit

import streamlit as st
st.title("Login Page")
username = st.text_input('Enter Username') 
password = st.text_input('Enter Password', type='password')
if st.button('LOGIN'):
    if username == 'lalit' and password == 'lalit@123':
        st.success('Login Successful!')
    elif username != 'lalit':
        st.error('Invalid Username')
    else:
        st.error('Invalid Password')
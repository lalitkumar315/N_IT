# My First Streamlit App 

import streamlit as st
st.title("My First Streamlit App")
st.write("Happy New Year")
st.header("WELCOME")
st.text("Enter your details below:")
name = st.text_input("Name")
age = st.number_input("Age")
st.selectbox("What you want to select", ["ADD", "SUB"])
st.checkbox("ADD")
st.checkbox("SUB")
st.radio("What you want to select", ["ADD", "SUB"])
st.button("Submit")
st.success("Details Submitted Successfully.")
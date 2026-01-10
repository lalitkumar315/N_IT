# wap to calculate tax ammount from salary and tax percentage using streamlit

import streamlit as st
st.title("Tax Amount Calculator App")
salary = st.number_input('Enter the Salary Amount')
tax_per = st.number_input('Enter the Tax percentage (%)')
if st.button('CALCULATE'):
    tax_amount = (salary * tax_per) / 100
    st.text('Result:')
    st.success(f'The tax amount on a salary of {salary} at a tax rate of {tax_per}% is {tax_amount}')
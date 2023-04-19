import streamlit as st

st.header('Selectbox')

option = st.selectbox(
    "what is your favorite color?",
    ("blue","red","green"))

st.write("You favorite color is:", option)
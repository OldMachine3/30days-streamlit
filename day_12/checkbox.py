import streamlit as st

st.header("Checkbox")

st.write("what would you like to order?")

icecream = st.checkbox("Ice Cream")
coffee = st.checkbox("Coffe")
cola = st.checkbox("Cola")

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
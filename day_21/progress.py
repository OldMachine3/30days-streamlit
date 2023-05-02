import streamlit as st
import time 

st.title("Progress bar example")

with st.expander("about this app"):
    st.write("You can now display a progress of your calculation in a streamlit app with the 'st.progress' command")
    
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1)

st.balloons()
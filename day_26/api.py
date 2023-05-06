# crate bored api

import streamlit as st
import requests

st.title("Bored API")

st.sidebar.header("Input")
selected_type = st.sidebar.selectbox("select an activity type", ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
    with st.expander("About this App"):
        st.write("Are you bored? the **Bored API app** provides suggestions on activites that you can do when you are bored. This app is powered by the Bored API.")
with c2:
    with st.expander("JSON data"):
        st.write(suggested_activity)
        
st.header("Suggested Activity")
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Number of Participants", value=suggested_activity['participants'], delta='')
with col2:
    st.metric(label="Type of Activity", value= suggested_activity['type'].capitalize(), delta='')
with col3:
    st.metric(label="Price", value=suggested_activity['price'], delta='')
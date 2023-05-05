# st.cache allows you to optimize the performance of your Streamlit app.

import streamlit as st
import numpy as np 
import pandas as pd
from time import time

st.title("Use Cache in Streamlit")

# using cache
a0 = time()
st.subheader("using cache")

@st.cache(suppress_st_warning=True)
def load_data_a():
    df = pd.DataFrame(
        np.random.randn(200000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# not using cache
b0 = time()
st.subheader("Not using st.cache")

def load_data_b():
    df = pd.DataFrame(
        np.random.randn(200000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)

import streamlit as st

st.title("Form")

st.header("1. Example of using `with` notation")
st.subheader("Coffe machine")

with st.form("my_form"):
    st.subheader("**Order your coffe**")
    
    # input widgets
    coffe_bean_val = st.selectbox("Coffe bean",["Arabica","Robusta"])
    coffe_roast_val = st.selectbox("Coffe roast",["Light","Medium","Dark"])
    brewing_val = st.selectbox("Brewing",["Espresso","Drip","French press"])
    serving_type_val = st.selectbox("Serving fromat",['Hot', 'Iced','Frappe'])
    milk_val = st.select_slider("Milk intensity", ["None", "Low", "Medium", "High"])
    own_cup_val = st.checkbox("Bring own cup")
    
    submitted = st.form_submit_button("Submit") 
    
if submitted:
    st.markdown(f'''
                ☕ You have ordered:
                - Coffe bean: `{coffe_bean_val}`
                - Coffe roast: `{coffe_roast_val}`
                - Brewing: `{brewing_val}`
                - Serving type: `{serving_type_val}`
                - Milk: `{milk_val}`
                - Bring own cup: `{own_cup_val}`
                ''')
else:
    st.write("Place your order")
    

st.header("2. Example of object notation")

form = st.form("my_form_2")
selected_val = form.slider("select a value")
form.form_submit_button("Submit")

st.write("Selected value:", selected_val)

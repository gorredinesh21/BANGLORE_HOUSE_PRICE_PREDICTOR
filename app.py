import streamlit as st
import json
import pandas as pd
import price

json_path="columns.json"


with open(json_path, "r") as f:
        data = json.load(f)

all_columns = data["columns"]

locations=all_columns[3:]
#total_sqft
#bath
#bhk
#location_name

st.title("Banglore Home Price Prdeictor")

total_sqft=st.number_input("ENTER THE APPROXIMATE  AMOUNT OF SQUARE FEET THAT YOU DESIRE ",step=1, format="%d")
bath=st.number_input("ENTER THE NUMBER OF BATHROOMS THAT YOU DESIRE ",step=1, format="%d")
bhk=st.number_input("ENTER THE NUMBER OF BEDROOMS THAT YOU DESIRE ",step=1, format="%d")
location_name=st.selectbox("SELECT THE LOCATION",locations)

submit_button = st.button("Submit")


#st.markdown('<h1>This is a very large text</h1>', unsafe_allow_html=True)

if submit_button:
    if None not in (total_sqft, bath, bhk, location_name):
        amount=price.predict(total_sqft,bath,bhk,location_name)[0]
        amount=round(amount,2)
        st.markdown(f"""
        <h1>The price of a flat at {location_name} having {bhk} bedrooms, {bath} bathrooms, and also having {total_sqft} square feet area is {amount} Lakhs</h1>""", unsafe_allow_html=True)
    else:
        st.write("Please fill in all the values before submitting.")



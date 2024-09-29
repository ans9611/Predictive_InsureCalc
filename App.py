# Importing Necessary Libraries
import numpy as np
import pandas as pd
import streamlit as st
import fickling

# Load the trained model
model = fickling.load(open('PIC.pkl', 'rb'))

# App header
st.header('Predictive Insurance Premium Calculator')

# User inputs for model prediction
name = st.text_input('Enter Your Name')
gender = st.selectbox('Choose Gender', ['Female', 'Male'])
smoker = st.selectbox('Are you a smoker?', ['Yes', 'No'])
region = st.selectbox(
    'Choose Region', ['SouthEast', 'SouthWest', 'NorthEast', 'NorthWest'])
age = st.slider('Enter Age', 5, 80)
bmi = st.slider('Enter BMI', 5, 100)
children = st.slider('Choose No of Children', 0, 5)

# Predict button
if st.button('Predict'):
    # Convert categorical inputs to numerical
    gender = 0 if gender == 'Female' else 1
    smoker = 1 if smoker == 'Yes' else 0

    # Encode regions into numerical values
    region_dict = {'SouthEast': 0, 'SouthWest': 1,
                   'NorthEast': 2, 'NorthWest': 3}
    region_encoded = region_dict[region]

    # Prepare the input data as a NumPy array
    input_data = (age, gender, bmi, children, smoker, region_encoded)
    input_data_array = np.asarray(input_data).reshape(1, -1)

    # Predict the insurance premium using the model
    predicted_prem = model.predict(input_data_array)

    # Display the result
    display_string = f'Insurance Premium will be {round(predicted_prem[0], 2)} USD Dollars'
    st.markdown(display_string)

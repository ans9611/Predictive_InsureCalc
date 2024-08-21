import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st
import smtplib
from email.mime.text import MIMEText

# Load the trained model using pickle
model = pkl.load(open('PIC.pkl', 'rb'))

# Streamlit header for the web application
st.header('Predictive Insurance Premium Calculator')

# User inputs for model prediction
name = st.text_input('Enter Your Name')

sex = st.selectbox('Choose Gender', ['Female', 'Male'])

smoker = st.selectbox('Are you a smoker?', ['Yes', 'No'])

region = st.selectbox(
    'Choose Region', ['SouthEast', 'SouthWest', 'NorthEast', 'NorthWest'])

age = st.slider('Enter Age', 5, 80)

bmi = st.slider('Enter BMI', 5, 100)

children = st.slider('Choose Number of Children', 0, 5)

# Predict button triggers the model prediction
if st.button('Predict'):
    # Encoding user inputs for model prediction
    sex = 0 if sex == 'Female' else 1
    smoker = 1 if smoker == 'Yes' else 0
    region = {'SouthEast': 0, 'SouthWest': 1,
              'NorthEast': 2, 'NorthWest': 3}[region]

    # Preparing the input data as a DataFrame with the same feature names used during training
    input_data = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                              columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

    # Predicting the insurance premium using the pre-trained model
    predicted_prem = model.predict(input_data)
    display_string = f'Insurance Premium for {name} will be {round(predicted_prem[0], 2)} USD Dollars'

    # Displaying the predicted premium in USD
    st.markdown(display_string)

    # Email input field
    email = st.text_input('Enter your email address to receive the result')

    # Send email button
    if st.button('Send Email'):
        if email:
            try:
                # Setup the MIME
                msg = MIMEText(display_string)
                msg['From'] = 'youremail@example.com'
                msg['To'] = email
                msg['Subject'] = 'Your Predicted Insurance Premium'

                # Send the email
                server = smtplib.SMTP('smtp.example.com', 587)
                server.starttls()
                server.login('youremail@example.com', 'yourpassword')
                server.sendmail('youremail@example.com',
                                email, msg.as_string())
                server.quit()

                st.success('Email sent successfully!')
            except Exception as e:
                st.error(f'Failed to send email. Error: {e}')
        else:
            st.error('Please enter a valid email address.')

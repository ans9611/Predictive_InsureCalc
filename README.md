# Predictive Insurance Premium Calculator

Welcome to Predictive Insurance Premium Calculator, a machine learning-driven application designed to predict medical insurance premiums based on user input. This project leverages cutting-edge technology to provide accurate and personalized premium estimates, enhancing decision-making for both insurers and policyholders.

## Project Overview

Predictive Insurance Premium Calculator is a full-stack application that combines a user-friendly interface with a robust backend to deliver quick and reliable insurance premium predictions. Built using React for the frontend and Flask for the backend, this app integrates a machine learning model trained on real-world data to offer insights into premium calculations.

## Features

- **User Input Interface:** Intuitive sliders and dropdowns for entering age, gender, BMI, smoking status, region, and number of children.
- **Real-time Predictions:** Instant premium predictions displayed upon user input submission.
- **Data Visualization:** Interactive charts showing how different factors influence premium costs.
- **Secure Data Handling:** Ensures user data privacy and secure transactions.

## Technology Stack

- **Frontend:** React, Streamlit for interactive UI
- **Backend:** Flask, Python
- **Machine Learning:** Scikit-learn for model training and prediction
- **Database:** MongoDB for storing user inputs and predictions
- **Deployment:** Deployed on Heroku for easy access

## Installation

Clone the repository:

```bash
git clone https://github.com/ans9611/PacificWave-PremiumPredictor.git
```
## About the Insurance Dataset

This dataset offers comprehensive information about insurance customers, including details such as age, sex, body mass index (BMI), number of children, smoking status, and region. These insights provide a valuable opportunity for analysts to better understand customer behavior and the factors influencing insurance charges. By examining patterns within the dataset, we can gain meaningful insights into how age, gender, and lifestyle choices impact a person’s insurance premiums. This understanding is crucial when developing insurance plans or designing marketing campaigns targeting specific demographics. Additionally, the dataset allows us to explore critical questions, such as identifying potential strategies for increasing affordability and addressing high charges for certain groups.

## Usage

### Input Details:
- **Name**
- **Gender** (Female/Male)
- **Smoker status** (Yes/No)
- **Region** (SouthEast, SouthWest, NorthEast, NorthWest)
- **Age** (slider input between 5 to 80 years)
- **BMI** (slider input between 5 to 100)
- **Number of children** (slider input between 0 to 5)

### Prediction:
- After entering the details, click on the **Predict** button.
- The application will display the predicted insurance premium in USD.

## Model Details
- The model used for prediction is a Random Forest Regressor trained on a dataset that includes features like age, gender, BMI, number of children, smoking status, and region.
- The notebook `Predictive_InsureCalc.ipynb` contains the code for data preprocessing, model training, and evaluation.

## Contributing
Contributions are welcome! If you'd like to improve this project, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### A Study of Customers' Insurance Charges  
By Bob Wakefield  
[Source](https://data.world/bob-wakefield/insurance)  
[Dataset Query Link](https://query.data.world/s/u7szctwylktrfrhorbylglddxq4k2p?dws=00000)

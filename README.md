# Bangalore House Price Prediction

## Project Overview
The House Price Prediction Model is a machine learning algorithm designed to estimate the selling price of residential properties in Bangalore based on relevant features. Using historical data, the model learns patterns and relationships between input variables, such as location, size, amenities, and age of the property, to make accurate price predictions.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Cleaning](#data-cleaning)
- [Feature Scaling](#feature-scaling)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Machine Learning Models](#machine-learning-models)
- [Model Evaluation](#model-evaluation)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Data Cleaning
- Removed missing values and handled outliers.
- Converted categorical variables into numerical format using one-hot encoding.

## Feature Scaling
- Applied feature scaling techniques such as Min-Max scaling or Standardization to normalize the input features.

## Exploratory Data Analysis (EDA)
- Visualized data distributions and relationships using various plots (scatter plots, heatmaps, etc.).
- Analyzed correlations between features and the target variable (house prices).

## Machine Learning Models
- Built several machine learning models to predict house prices, including:
  - **Linear Regression**
  - **Regression Tree**
  - **Random Forest Regressor**
  
- **Grid Search Cross-Validation** was performed to optimize hyperparameters and improve model performance.

## Model Evaluation
- Evaluated model performance using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.

## Installation
To set up the project locally, clone the repository and install the required packages:

## Usage 
-Run the following command to execute the prediction model:
- python app.py


```bash
git clone https://github.com/gorredinesh_21/BANGLORE_HOUSE_PRICE_PREDICTOR.git
cd BANGLORE_HOUSE_PRICE_PREDICTOR
pip install -r requirements.txt




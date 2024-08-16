import json
import numpy as np
import pandas as pd
import pickle
json_path="columns.json"

def predict(total_sqft, bath, bhk, location_name ):
    with open(json_path, "r") as f:
        data = json.load(f)
    all_columns = data["columns"]
    
    # Initialize the input array with zeros
    input_array = np.zeros(len(all_columns))
    
    # Set values for total_sqft, bath, and bhk
    input_array[all_columns.index('total_sqft')] = total_sqft
    input_array[all_columns.index('bath')] = bath
    input_array[all_columns.index('bhk')] = bhk
    
    # Set the corresponding location to 1 if it exists in the columns
    location_name=location_name.lower()
    if location_name in all_columns:
        input_array[all_columns.index(location_name)] = 1
    
    input_df = pd.DataFrame([input_array], columns=all_columns)
    # Make the prediction
    model_path="banglore_home_prices_model.pickle"

    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    predicted_price = model.predict(input_df)
    return predicted_price

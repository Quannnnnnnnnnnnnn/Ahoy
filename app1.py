import streamlit as st
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the model
model = load_model('/mnt/data/houseprice.keras')

# Load the feature list (already loaded as features_data)
# features_data contains the list of features

# Create a Streamlit form for user input
st.title("House Price Prediction")
st.subheader("Please enter the details of the house:")

# Create input fields for all the features
input_features = {}
for feature in features_data:
    input_features[feature] = st.text_input(feature, "")

# Button to make a prediction
if st.button('Predict Price'):
    # Prepare the input data to match the format expected by the model
    # We assume here that the inputs are numerical, if not, you may need to preprocess or encode
    input_data = []
    for feature in features_data:
        try:
            input_data.append(float(input_features[feature]))
        except ValueError:
            input_data.append(0.0)  # Default to 0 if the input is not a valid number

    # Reshape the input to match the model input shape
    input_data = [input_data]

    # Predict the house price using the model
    prediction = model.predict(input_data)

    # Display the prediction result
    st.subheader(f"Predicted House Price: ${prediction[0][0]:,.2f}")

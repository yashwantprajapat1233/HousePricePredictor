import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model and features
model = joblib.load('random_forest_model.pkl')
feature_columns = joblib.load('model_features.pkl')

st.set_page_config(page_title="🏠 House Price Predictor", layout="centered")
st.title("🏡 California House Price Predictor")
st.markdown("Use the sliders and dropdown to predict median house value.")

# User inputs
longitude = st.slider("Longitude", -125.0, -113.0, -120.0)
latitude = st.slider("Latitude", 32.0, 43.0, 36.0)
housing_median_age = st.slider("Housing Median Age", 1, 52, 20)
total_rooms = st.slider("Total Rooms", 100, 10000, 2000)
total_bedrooms = st.slider("Total Bedrooms", 1, 2000, 300)
population = st.slider("Population", 10, 20000, 1500)
households = st.slider("Households", 1, 5000, 500)
median_income = st.slider("Median Income", 0.5, 15.0, 4.0)

# Dropdown for ocean proximity
ocean_proximity = st.selectbox("Ocean Proximity", [
    '<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'
])

# One-hot encode the selected category
ocean_prox_encoded = {
    '<1H OCEAN': [1, 0, 0, 0, 0],
    'INLAND':    [0, 1, 0, 0, 0],
    'ISLAND':    [0, 0, 1, 0, 0],
    'NEAR BAY':  [0, 0, 0, 1, 0],
    'NEAR OCEAN': [0, 0, 0, 0, 1]
}

# Combine all inputs
input_data = np.array([[
    longitude, latitude, housing_median_age, total_rooms, total_bedrooms,
    population, households, median_income,
    *ocean_prox_encoded[ocean_proximity]
]])

# Ensure correct column alignment
input_df = pd.DataFrame(input_data, columns=feature_columns)

# Predict
if st.button("Predict House Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"🏷️ Predicted Median House Value: **${int(prediction):,}**")

st.markdown("---")
st.caption("Made with ❤️ by Yashwant Prajapat")

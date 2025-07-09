import streamlit as st
import joblib
import numpy as np
import os

# Load model and feature names
MODEL_PATH = "random_forest_model.pkl"
FEATURES_PATH = "model_features.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(FEATURES_PATH):
    st.error("Model files not found. Please ensure the model and features files are present.")
    st.stop()

model = joblib.load(MODEL_PATH)
features = joblib.load(FEATURES_PATH)

st.set_page_config(page_title="California House Price Predictor", layout="centered")

st.title("🏠 California House Price Predictor")
st.markdown("Enter the details of the house in the sidebar to predict its **market price** in California.")

# Sidebar input
st.sidebar.header("🏡 Input House Details")

inputs = []
for feature in features:
    value = st.sidebar.number_input(f"{feature}", value=0.0, step=1.0)
    inputs.append(value)

# Predict button
if st.sidebar.button("🔮 Predict Price"):
    try:
        input_array = np.array(inputs).reshape(1, -1)
        prediction = model.predict(input_array)
        st.success(f"💰 Estimated House Price: **${prediction[0]:,.2f}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

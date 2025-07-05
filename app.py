import streamlit as st
import numpy as np
import pickle

# Load model and scaler using pickle
with open("wine_quality_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Page settings
st.set_page_config(page_title="Wine Quality Predictor", page_icon="🍷")
st.markdown(
    "<h1 style='text-align: center; color: #8B0000;'>🍷 Boutique Wine Quality Prediction</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Enter wine chemical data to check if it meets premium quality standards.</p>",
    unsafe_allow_html=True
)

# Input layout in columns
features = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide',
    'density', 'pH', 'sulphates', 'alcohol'
]

cols = st.columns(3)
user_inputs = []

for i, feature in enumerate(features):
    with cols[i % 3]:
        val = st.number_input(f"{feature.title()}", format="%.4f")
        user_inputs.append(val)

# Predict button
if st.button("🔍 Predict Quality"):
    input_array = np.array(user_inputs).reshape(1, -1)
    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)[0]
    confidence = model.predict_proba(input_scaled)[0][prediction]

    st.markdown("---")
    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("✅ This wine is **Good Quality**")
    else:
        st.error("❌ This wine is **Not Good Quality**")

    st.metric(label="Confidence Score", value=f"{confidence * 100:.2f}%")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 13px;'>Developed by <strong>KNTG</strong> for Boutique Winery QA Team</p>",
    unsafe_allow_html=True
)

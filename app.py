import streamlit as st
import numpy as np

st.set_page_config(page_title="Yield & Price Forecasting AI")

st.title("🌾 Yield & Price Forecasting AI Agent")

st.write("Enter crop details to predict yield & price")

crop = st.selectbox("Crop Name", ["Rice", "Wheat", "Maize", "Cotton"])
area = st.number_input("Area (Acres)", min_value=1.0)
rainfall = st.slider("Rainfall (mm)", 0, 300)
demand = st.slider("Market Demand (%)", 0, 100)

if st.button("Predict"):
    # Simple AI logic
    yield_prediction = area * (rainfall / 100) * 2
    price_prediction = 20 + (demand * 0.8)

    st.success(f"🌱 Estimated Yield: {yield_prediction:.2f} tons")
    st.success(f"💰 Estimated Price: ₹{price_prediction:.2f} per kg")

    st.info("⚠ This is an AI-based estimation, not exact market value")

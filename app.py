import streamlit as st
import pandas as pd

st.title("📦 Smart Inventory Demand Predictor")

# Upload dataset
file = st.file_uploader("Upload CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    
    st.subheader("📊 Data Preview")
    st.write(df)

    if "Sales" in df.columns:
        # Simple prediction logic
        df["Predicted_Demand"] = df["Sales"].rolling(window=2).mean()

        st.subheader("📈 Demand Prediction")
        st.line_chart(df[["Sales", "Predicted_Demand"]])

        st.write(df)
    else:
        st.error("Dataset must contain 'Sales' column")
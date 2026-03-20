import streamlit as st
import pandas as pd

st.title("🍽️ Food Quality Tracking Dashboard")

# Sample data (you can replace later)
data = {
    "Batch_ID": [101, 102, 103, 104],
    "Product": ["Milk", "Bread", "Cheese", "Juice"],
    "Quality_Status": ["Good", "Defective", "Good", "Defective"],
    "Defects": [0, 2, 0, 1]
}

df = pd.DataFrame(data)

st.subheader("📊 Product Quality Data")
st.write(df)

# Filter defective products
st.subheader("⚠️ Defective Products")
defective = df[df["Quality_Status"] == "Defective"]
st.write(defective)

# Chart
st.subheader("📈 Defects by Product")
st.bar_chart(df.set_index("Product")["Defects"])
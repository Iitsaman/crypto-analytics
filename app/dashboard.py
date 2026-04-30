import streamlit as st
import pandas as pd
from api import get_crypto_data

st.title("Crypto Analytics Dashboard")

coin = st.selectbox("Choose a coin", ["bitcoin", "ethereum"])
df = get_crypto_data(coin)

df["ma_7"] = df["price"].rolling(7).mean()

st.subheader("Price & 7-day Moving Average")
st.line_chart(df.set_index("timestamp")[["price", "ma_7"]])

st.subheader("Volume")
st.bar_chart(df.set_index("timestamp")["volume"])

df["volume"] = df["volume"].round(2)   
df["price"] = df["price"].round(2)     
df["ma_7"] = df["ma_7"].round(2)


st.subheader("Raw Data")
st.dataframe(df)
import pandas as pd
import plotly.express as px
import streamlit as st

def display_table3(data):
    st.write("This is Table 3: Exchange Rates and Market Capitalization on 20/03/2020.")
    data.columns = ["Currency", "Sell", "Buy", "Average"]

    exchange_data = data.iloc[:-1]  # All rows except the last for exchange rates
    market_cap = data.iloc[-1, 0]  # Last row, first column for Market Capitalization

    st.subheader("Exchange Rates")
    st.write(exchange_data)

    st.subheader("Market Capitalization (Frw)")
    st.write(market_cap)

    fig = px.bar(exchange_data, x="Currency", y="Average", title="Average Exchange Rate by Currency")
    st.plotly_chart(fig)

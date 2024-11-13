import pandas as pd
import plotly.express as px
import streamlit as st

def display_table2(data):
    st.write("This is Table 2: Indices and Other Trading Statistics.")
    data.columns = ["Indices", "Previous", "Today", "Points", "Change %"]
    st.write(data)

    indices_data = data.iloc[:2]  # First two rows for INDICES
    other_trading_data = data.iloc[2:]  # Remaining rows for OTHER TRADING STAT

    st.subheader("INDICES")
    st.write(indices_data)

    st.subheader("OTHER TRADING STAT")
    st.write(other_trading_data)

    fig = px.bar(indices_data, x="Indices", y="Change %", title="Change % in Indices")
    st.plotly_chart(fig)

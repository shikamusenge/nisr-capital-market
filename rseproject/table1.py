import pandas as pd
import plotly.express as px
import streamlit as st

def display_table1(data):
    st.write("This is Table 1: Equities Market on 20/03/2020.")
    data.columns = ["ISIN-Code", "Stock", "12M High", "12M Low", "Today High", "Today Low",
                    "Closing", "Previous", "Change", "Volume", "Value"]
    st.write(data)

    fig = px.bar(data, x="Stock", y="Closing", title="Closing Prices by Stock")
    st.plotly_chart(fig)

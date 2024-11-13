import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import datetime

def display_table4(data):
    st.write("This is Table 4 data.")
    data.columns = ["ISIN-Code", "Status", "Security", "Maturity", "Coupon rate",
                    "Close Price", "Prev. Price", "Bids", "Offers", "Bond traded"]
    data['Maturity'] = pd.to_datetime(data['Maturity'], errors='coerce')
    data['Close Price'] = pd.to_numeric(data['Close Price'], errors='coerce')

    st.sidebar.header("🔍 Search & Filter Options for Table 4")

    # Search by Security Name
    stock_name = st.sidebar.text_input("Search by Security Name:")
    filtered_data = data[data['Security'].str.contains(stock_name, case=False, na=False)]

    # Set up date filtering range for Maturity date
    min_date = data['Maturity'].min().date() if data['Maturity'].notnull().any() else datetime(2021, 1, 1).date()
    max_date = data['Maturity'].max().date() if data['Maturity'].notnull().any() else datetime(2035, 1, 1).date()
    start_date = st.sidebar.date_input("Start Date", value=min_date, min_value=min_date, max_value=max_date)
    end_date = st.sidebar.date_input("End Date", value=max_date, min_value=start_date, max_value=max_date)

    # Filter data based on selected date range
    filtered_data = filtered_data[(filtered_data['Maturity'] >= pd.to_datetime(start_date)) &
                                  (filtered_data['Maturity'] <= pd.to_datetime(end_date))]

    st.write(filtered_data)

    if not filtered_data.empty:
        fig = px.line(filtered_data, x="Maturity", y="Close Price", color="Security", title="Close Price Over Time by Security")
        st.plotly_chart(fig)
    else:
        st.warning("No data available for the selected filters.")

    fig2 = px.bar(filtered_data, x="Security", y="Coupon rate", color="Coupon rate", title="Coupon Rate Comparison by Security")
    st.plotly_chart(fig2)

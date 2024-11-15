import pandas as pd
import plotly.express as px
import streamlit as st

# Set up custom styling for the app
st.markdown("""
    <style>
    .heading {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 25px;
        font-weight: 300;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .table-container {
        padding: 10px;
        border-radius: 10px;
        background-color: #f4f4f4;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .chart-container {
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Function to display Table 1
def display_table1(data):
    # Add a styled heading
    st.markdown('<div class="heading">Rwanda Stock Exchange</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Equities Market Data on 20/03/2020</div>', unsafe_allow_html=True)

    # Clean up the data table and add some styling
    data.columns = ["ISIN-Code", "Stock", "12M High", "12M Low", "Today High", "Today Low",
                    "Closing", "Previous", "Change", "Volume", "Value"]

    # Display the table with styling
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.write(data)
    st.markdown('</div>', unsafe_allow_html=True)

    # Plot the Closing Prices by Stock
    fig = px.bar(data, x="Stock", y="Closing", title="Closing Prices by Stock",
                 color="Stock", labels={"Stock": "Stock Symbol", "Closing": "Closing Price"})

    # Enhance the chart with a style update
    fig.update_layout(
        title="Closing Prices by Stock",
        title_x=0.5,  # Center the title
        plot_bgcolor="#f9f9f9",  # Light background for the chart
        xaxis=dict(showgrid=False, title="Stock Symbols", title_font=dict(size=14)),
        yaxis=dict(showgrid=True, title="Price (RWF)", title_font=dict(size=14)),
        bargap=0.1,  # Space between bars
        template="plotly_dark"  # A dark theme for a more modern look
    )

    # Display the chart inside a container
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.plotly_chart(fig)
    st.markdown('</div>', unsafe_allow_html=True)

# Example usage: Call the function with sample data
if __name__ == "__main__":
    # Sample data
    data = pd.DataFrame({
        "ISIN-Code": ["RSE1", "RSE2", "RSE3", "RSE4"],
        "Stock": ["Stock A", "Stock B", "Stock C", "Stock D"],
        "12M High": [150, 200, 170, 180],
        "12M Low": [120, 140, 130, 160],
        "Today High": [148, 195, 168, 178],
        "Today Low": [125, 145, 135, 160],
        "Closing": [145, 190, 165, 175],
        "Previous": [140, 185, 160, 170],
        "Change": [5, 5, 5, 5],
        "Volume": [1000, 2000, 1500, 1800],
        "Value": [5000, 4000, 4500, 5500]
    })

    display_table1(data)

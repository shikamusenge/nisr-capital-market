import pandas as pd
import plotly.express as px
import streamlit as st

# Custom CSS to enhance design
st.markdown("""
    <style>
    .header {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 25px;
        font-weight: 300;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .table-container {
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
    }
    .plot-container {
        margin-top: 40px;
    }
    .chart {
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Function to display Table 3 and Chart
def display_table3(data):
    # Title and subtitle with custom styling
    st.markdown('<div class="header">Rwanda Stock Exchange</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Exchange Rates and Market Capitalization on 20/03/2020</div>', unsafe_allow_html=True)

    # Rename columns for better readability
    data.columns = ["Currency", "Sell", "Buy", "Average"]

    # Split the data into exchange rates and market capitalization
    exchange_data = data.iloc[:-1]  # All rows except the last for exchange rates
    market_cap = data.iloc[-1, 0]  # Last row, first column for Market Capitalization

    # Display the exchange rates data
    st.subheader("Exchange Rates")
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.write(exchange_data)
    st.markdown('</div>', unsafe_allow_html=True)

    # Display the market capitalization data
    st.subheader("Market Capitalization (Frw)")
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.write(market_cap)
    st.markdown('</div>', unsafe_allow_html=True)

    # Create a bar chart for Average Exchange Rate by Currency
    fig = px.bar(exchange_data, x="Currency", y="Average", title="Average Exchange Rate by Currency")

    # Customize the chart layout
    fig.update_layout(
        title="Average Exchange Rate by Currency",
        title_x=0.5,  # Center title
        plot_bgcolor="#ffffff",  # White background for clarity
        xaxis=dict(showgrid=False, title="Currency", title_font=dict(size=14)),
        yaxis=dict(showgrid=True, title="Average Rate", title_font=dict(size=14)),
        template="plotly_white",  # White theme for clarity
        margin=dict(l=50, r=50, t=50, b=50)  # Adjust margins
    )

    # Display the chart in a styled container
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Example usage: call the function with sample data
if __name__ == "__main__":
    # Sample data for Table 3
    data = pd.DataFrame({
        "Currency": ["USD", "EUR", "GBP", "Market Cap"],
        "Sell": [1000, 1200, 1400, None],
        "Buy": [980, 1180, 1380, None],
        "Average": [990, 1190, 1390, None]
    })

    display_table3(data)

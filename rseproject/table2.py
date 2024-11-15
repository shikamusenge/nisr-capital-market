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

# Function to display Table 2 and Chart
def display_table2(data):
    # Title and subtitle with custom styling
    st.markdown('<div class="header">Rwanda Stock Exchange</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Indices and Other Trading Statistics</div>', unsafe_allow_html=True)

    # Rename columns for better readability
    data.columns = ["Indices", "Previous", "Today", "Points", "Change %"]

    # Display the data in a styled container
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.write(data)
    st.markdown('</div>', unsafe_allow_html=True)

    # Split the data into INDICES and OTHER TRADING STAT
    indices_data = data.iloc[:2]  # First two rows for INDICES
    other_trading_data = data.iloc[2:]  # Remaining rows for OTHER TRADING STAT

    # Display Indices section with custom styling
    st.subheader("INDICES")
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.write(indices_data)
    st.markdown('</div>', unsafe_allow_html=True)

    # Display Other Trading Statistics section with custom styling
    st.subheader("OTHER TRADING STAT")
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.write(other_trading_data)
    st.markdown('</div>', unsafe_allow_html=True)

    # Create a bar chart for Change % in Indices
    fig = px.bar(indices_data, x="Indices", y="Change %", title="Change % in Indices")

    # Customize the chart layout
    fig.update_layout(
        title="Change % in Indices",
        title_x=0.5,  # Center title
        plot_bgcolor="#ffffff",  # White background for clarity
        xaxis=dict(showgrid=False, title="Indices", title_font=dict(size=14)),
        yaxis=dict(showgrid=True, title="Change %", title_font=dict(size=14)),
        template="plotly_white",  # White theme for clarity
        margin=dict(l=50, r=50, t=50, b=50)  # Adjust margins
    )

    # Display the chart in a styled container
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Example usage: call the function with sample data
if __name__ == "__main__":
    # Sample data for Table 2
    data = pd.DataFrame({
        "Indices": ["Index A", "Index B", "Stat A", "Stat B", "Stat C"],
        "Previous": [1000, 1200, 1500, 1800, 1600],
        "Today": [1020, 1215, 1510, 1790, 1580],
        "Points": [20, 15, 10, -10, -20],
        "Change %": [2.0, 1.25, 0.67, -0.56, -1.25]
    })

    display_table2(data)

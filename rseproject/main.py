import streamlit as st
import pandas as pd
import plotly.express as px

# Import individual table display functions
from table1 import display_table1
from table2 import display_table2
from table3 import display_table3
from table4 import display_table4
from youth_data import load_youth_data  # Import the youth data loading function

# Load all sheets from the Excel file into a dictionary of DataFrames
sheets = pd.read_excel('dat.xlsx', sheet_name=None)

# Add a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", list(sheets.keys()) + ["Youth Data"])  # Add "Youth Data" to navigation options

# Display the content of the selected page
st.title(f"📄 Data from {page}")

# Display the appropriate table or visualization based on the selected page
if page == "Table 1":
    display_table1(sheets["Table 1"])
elif page == "Table 2":
    display_table2(sheets["Table 2"])
elif page == "Table 3":
    display_table3(sheets["Table 3"])
elif page == "Table 4":
    display_table4(sheets["Table 4"])
elif page == "Youth Data":
    # Load youth data and visualize it
    st.title("📊 Youth Labor Statistics Over Quarters (2019-2024)")
    st.subheader("Data Table")

    # Load youth data
    youth_data = load_youth_data()
    st.dataframe(youth_data, use_container_width=True)

    # Dropdown for metric selection
    st.subheader("📊 Metric Visualization")
    metric = st.selectbox("Select a metric to visualize", youth_data['Metric'].unique())

    # Filter data based on selected metric
    selected_data = youth_data[youth_data['Metric'] == metric]

    # Extract the time columns (e.g., '2019 (Q1)', '2019 (Q2)', ...) for the selected metric
    time_columns = selected_data.columns[1:]  # Skip the 'Metric' column
    values = selected_data.iloc[0, 1:].values  # Get the values for the selected metric

    # Create a DataFrame for plotting
    plot_data = pd.DataFrame({
        'Quarter': time_columns,
        'Value': values
    })

    # Plot the selected metric over time
    fig = px.line(plot_data, x='Quarter', y='Value', title=f"{metric} Over Time (2019-2024)")

    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)

else:
    st.write("No specific visualization configured for this sheet.")
    st.write(sheets[page])

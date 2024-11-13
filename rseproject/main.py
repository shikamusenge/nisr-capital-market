import pandas as pd
import streamlit as st

# Import individual table display functions
from table1 import display_table1
from table2 import display_table2
from table3 import display_table3
from table4 import display_table4

# Load all sheets from the Excel file into a dictionary of DataFrames
sheets = pd.read_excel('dat.xlsx', sheet_name=None)

# Add a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", list(sheets.keys()))

# Display the content of the selected page
st.title(f"📄 Data from {page}")

# Get the data for the selected sheet
data = sheets[page]

# Display the appropriate table based on the selected page
if page == "Table 1":
    display_table1(data)
elif page == "Table 2":
    display_table2(data)
elif page == "Table 3":
    display_table3(data)
elif page == "Table 4":
    display_table4(data)
else:
    st.write("No specific visualization configured for this sheet.")
    st.write(data)


Youth Unemployment solution with Rwanda Stock Exchange 


Project Overview
This project aims to leverage data from the Rwanda Stock Exchange (RSE) and youth unemployment statistics to identify trends, patterns, and correlations that could contribute to addressing the issue of youth unemployment in Rwanda. By analyzing and visualizing both datasets, the goal is to generate insights that can inform policies or initiatives aimed at reducing unemployment among young people in Rwanda.



Objective
The primary objective of this project is to:

Visualize key trends in youth unemployment.
Analyze how stock market performance and economic activity (as indicated by the Rwanda Stock Exchange) can potentially influence job creation or youth employment.


Use data-driven insights to explore possible solutions to reduce youth unemployment in Rwanda.
Dataset Sources
Rwanda Stock Exchange Data: This dataset includes information on stock prices, trading volumes, and other financial indicators of companies listed on the Rwanda Stock Exchange. The data is essential for understanding the economic performance of the market and its potential effects on employment.

Youth Unemployment Data: This dataset includes statistics on youth unemployment in Rwanda, providing insight into how many young people are unemployed, their age groups, educational background, and other relevant factors that might affect their ability to find employment.


Project Features
1. Data Collection and Preprocessing
Rwanda Stock Exchange Data: The stock exchange data is collected from publicly available sources (such as the official RSE website or financial data providers).
Youth Unemployment Data: Youth unemployment data is gathered from government reports, surveys, or international organizations such as the World Bank or UNDP.
Data Cleaning and Transformation: Both datasets will be cleaned and transformed to ensure they are ready for analysis.


2. Data Visualization
Stock Market Trends: Use graphs and charts to show trends in the Rwanda Stock Exchange, such as price movements, trading volumes, and performance over time.
Youth Unemployment Analysis: Visualizations to display the distribution of youth unemployment by age, gender, education, and other demographic factors.
Correlation Analysis: Visual representations to compare RSE data with youth unemployment trends, exploring if there is any correlation or patterns that can inform solutions.


3. Insights and Analysis
Exploring Economic Impacts: Analyze how changes in the stock market (such as increased market activity or investment in certain sectors) might affect youth employment opportunities.
Policy Suggestions: Based on the analysis, the project will propose possible policies or initiatives that could help reduce youth unemployment by encouraging investment in sectors that create jobs for young people.




cd path to \nisr-capital-market\rseproject


1) ######## Create virtual environment ##########

python -m venv myenv

myenv\Scripts\activate





2) ######## package to be installed ###########

pip install pandas streamlit plotly openpyxl


3) ########### to run this project #############
 
streamlit run main.py


import streamlit as st
import pandas as pd
import plotly.express as px


# Read the dataset’s CSV file into a Pandas DataFrame
df = pd.read_csv('vehicles_us_cleaned.csv')

# Streamlit app
st.title(':blue[*Car Sales Advertisements Analysis*]')

# Header
st.header('Exploratory Data Analysis')

intro_text = """
    <div style='color: #CC5500;'>
    <p>In this project, we analyze a dataset of car sales to uncover insights about car prices, model years, conditions, and types. 
    The dataset contains various attributes such as price, model year, condition, odometer reading, fuel type, transmission type, and more. 
    Our goal is to explore these attributes and understand the relationships between them to provide valuable insights for potential buyers, sellers, and market analysts.</p>
    </div>
"""
st.write(intro_text, unsafe_allow_html=True)

# Plotly Express histograms
st.subheader('Distribution of Car Prices')
fig_price = px.histogram(df, x='price', title='Distribution of Car Prices')
st.plotly_chart(fig_price)

st.subheader('Distribution of Car Model Years')
fig_model_year = px.histogram(df, x='model_year', title='Distribution of Car Model Years')
st.plotly_chart(fig_model_year)

# Checkbox to filter data by year
if st.checkbox('Filter data by year'):
    year_filter = st.slider('Select Year Range', int(df['model_year'].min()), int(df['model_year'].max()), (2000, 2020))
    filtered_df = df[(df['model_year'] >= year_filter[0]) & (df['model_year'] <= year_filter[1])]
    st.write(filtered_df)

# Checkbox to filter data by price
if st.checkbox('Filter data by price'):
    price_filter = st.slider('Select Price Range', int(df['price'].min()), int(df['price'].max()), (5000, 50000))
    filtered_df = df[(df['price'] >= price_filter[0]) & (df['price'] <= price_filter[1])]
    st.write(filtered_df)

# Checkbox to show distribution of car conditions
if st.checkbox('Show distribution of car conditions'):
    st.subheader('Distribution of Car Conditions')
    fig_condition = px.histogram(df, x='condition', title='Distribution of Car Conditions')
    st.plotly_chart(fig_condition)

# Plotly Express scatter plots
st.subheader('Price vs. Odometer')
fig_price_odometer = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer')
st.plotly_chart(fig_price_odometer)

st.subheader('Price vs. Model Year')
fig_price_model_year = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year')
st.plotly_chart(fig_price_model_year)

# Checkbox to show price vs. condition
if st.checkbox('Show Price vs. Condition'):
    st.subheader('Price vs. Condition')
    fig_price_condition = px.scatter(df, x='condition', y='price', title='Price vs. Condition')
    st.plotly_chart(fig_price_condition)

# Checkbox to show/hide additional information
if st.checkbox('Show more details about the data'):
    st.subheader('Detailed Data View')
    st.write(df.describe())
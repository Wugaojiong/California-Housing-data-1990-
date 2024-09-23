import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-v0_8')

st.title('California Housing Data (1990) by Gaojiong Wu')
df = pd.read_csv('housing.csv')
minimal_median_house_filter = st.slider('Minimal Median House Price:', 0, 500001, 200000)
st.header('See more filters in the sidebar')
ocean_proximity_filter = st.sidebar.multiselect(
     'Choose the location type', 
     df.ocean_proximity.unique(), 
     df.ocean_proximity.unique()    
)

income_level = st.sidebar.radio('Choose income level:', ['Low', 'Medium', 'High'])


df = df[df.median_house_value >= minimal_median_house_filter]

df = df[df.ocean_proximity.isin(ocean_proximity_filter)]

if income_level == 'Low':
    df = df[df.median_income <= 2.5]
elif income_level == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_level == 'High':
    df = df[df.median_income > 4.5]

st.map(df)


st.subheader('The histogram of the median house value')
fig, ax = plt.subplots(figsize=(20, 10))
df.median_house_value.plot.hist(ax=ax,bins=30,rwidth=1)
st.pyplot(fig)

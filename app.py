import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-v0_8')

st.title('California Housing Data (1990) by Gaojiong Wu')
df = pd.read_csv('housing.csv')
minimal_median_house_filter = st.slider('Minimal Median House Price:', 0, 500001, 200000)

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

st.subheader('Median house value')
fig, ax = plt.subplots(figsize=(20, 5))
fig, ax = plt.subplots(figsize=(20, 5))
plt.style.use('seaborn-v0_8')
median_value_counts = df['median_house_value'].value_counts().sort_index()
median_value_counts.plot.bar(ax=ax, width=0.8)
st.pyplot(fig)

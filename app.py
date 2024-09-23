import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.title('California Housing Data (1990) by Gaojiong Wu')
df = pd.read_csv('housing.csv')
minimal_median_house_filter = st.slider('Minimal Median House Price:', 0.0, 500001.0, 200000.0)

ocean_proximity_filter = st.sidebar.multiselect(
     'Choose the location type', 
     df.ocean_proximity.unique(), 
     df.ocean_proximity.unique()    
)

income_level = st.radio('Choose income level:', ['Low', 'Medium', 'High'])


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
df.median_house_value.hist(bins=30, ax=ax,rwidth=2)
st.pyplot(fig)

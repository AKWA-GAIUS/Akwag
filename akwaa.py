import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import pickle  #to load a saved model
import base64  #to open .gif files in streamlit app

st.title("Akwa Visualization App For Daywise Dataset")
st.header("Covid Visualization")
st.subheader("Daywise Dataset Available On Kaggle")
st.write("Coronavirus is a family of viruses that can cause illness, which can vary from common cold and cough to sometimes more severe disease. The number of new cases are increasing day by day around the world. This dataset has information from the states and union territories of USA at daily level.")

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value



st.image("covidd.jpg")
data=pd.read_csv("C:/Users/USER/OneDrive/Desktop/covid/day_wise.csv")
numeric_columns = list(data.select_dtypes(['float', 'int']).columns)
non_numeric_columns = list(data.select_dtypes(['object']).columns)
non_numeric_columns.append(None)
print(non_numeric_columns)

dt = data.drop(["Date"], axis=1)

st.write(data.head())
st.markdown("Bar Chart of various Attributes")
st.bar_chart(dt)

import plotly.express as px

agree= st.button("click to see Boxplot")
if agree:
    plot = px.box(data_frame=dt)
    st.plotly_chart(plot)
agree= st.button("click to see Area chart")
if agree:
    st.markdown("Area Chart of various Attributes")
    st.area_chart(dt)

agree= st.button("click to see line chart")
if agree:
    st.markdown("Line Chart of various Attributes")
    st.line_chart(dt)
 
agree= st.button("click to see Histogram")
if agree:
    st.sidebar.subheader("Histogram Settings")
    st.markdown('Histogram')
    x = st.sidebar.selectbox('Feature', options=numeric_columns)
    bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                                 max_value=100, value=40)
    color_value = st.sidebar.selectbox("Colored", options=non_numeric_columns)
    plot = px.histogram(x=x, data_frame=data, color=color_value)
    st.plotly_chart(plot)



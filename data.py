import streamlit as st
import pandas as pd
import numpy as np

n= np.arange(8)

print(n)

nd =n.reshape((2,4))

print(nd)

df1=pd.read_csv('sample_data1.csv')
df2=pd.read_csv('sample_data2.csv')
print(df1)

st.title('Numerical Data')
st.dataframe(df1)

st.title('Categorical data')
st.write(df2)
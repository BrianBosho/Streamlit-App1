import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

df1=pd.read_csv('sample_data1.csv')
df2=pd.read_csv('sample_data2.csv')

st.image('pp.jpg')
# print(df1)
print(df1.columns)
print(df2.columns)
filt=df1['advert_price']<df1['advert_price'].quantile(0.75)
x=df1.loc[filt]['advert_price']
plt.hist(x)
st.pyplot()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

df1 = pd.read_csv('sample_data1.csv')
df2 = pd.read_csv('sample_data2.csv')

col = st.sidebar.selectbox('Select a parameter', df1.columns[1:])
option = st.sidebar.selectbox('Use Log',( True, False))
number = st.sidebar.number_input('Enter Percentile', step=15)


def plot_hist(column_name, log_scale, quantile, data):
    max = data[column_name].quantile(quantile)
    filt = data[column_name] < max
    x = data.loc[filt][column_name]

    plt.title(f'Distribution for {column_name}')
    plt.xlabel(f'{column_name}')
    plt.ylabel('Number of Items')

    # Add the median & mean lines
    median_price = x.median()
    mean_price = x.mean()
    plt.axvline(median_price, color='black', label='Median')
    plt.axvline(mean_price, color='red', label='Mean')

    # Plot the hist
    plt.legend()

    plt.hist(x, bins=20, log=log_scale, edgecolor='white')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


plot_hist(col, option, number/100, df1)



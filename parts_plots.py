import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

pd.set_option('display.max_columns', 50)
# matplotlib figures styling
plt.rcParams['figure.figsize'] = [10, 5]
plt.style.use('fivethirtyeight')

df = pd.read_csv('basic_parts_data.csv')

ls_product_cat = ['Type', 'Subtype', 'seller name', 'package', 'Condition', 'Make', 'location', 'region']
ls_product_num = ['price', 'inquires', 'listing duration', 'moderated duration', 'views']


def plot_hist(column_name, log_scale, quantile, data):
    max = data[column_name].quantile(quantile)
    filt = data[column_name] < max
    x = data.loc[filt][column_name]

    plt.title(f'Distribution for {column_name.capitalize()}')
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


def plot_group_bars(column_name, log_scale, data):
    # Step 1 Create a df based on the categorical variable
    data = data[column_name].value_counts().rename_axis(column_name).to_frame('counts').reset_index()

    # step 2: get the variables to do the plots:
    x = data[column_name][:20]
    y = data['counts'][:20]
    total = data['counts'].sum()

    # step3 add details to the plots:
    plt.title(f'{column_name.capitalize()} (Total: {total})')
    plt.xlabel(column_name.capitalize())
    plt.ylabel('No. of Products')
    plt.xticks(rotation=90)

    if log_scale:
        plt.yscale('log')

    plt.bar(x, y)
    st.pyplot()


nav = st.sidebar.radio('Select Plots', ('Bars', 'Histograms'))

if nav == 'Bars':
    st.title('Bars')
    col2 = st.sidebar.selectbox('Select a parameter', ls_product_cat)
    option = st.sidebar.selectbox('Use Log', (False, True))
    # number = st.sidebar.number_input('Enter Percentile', step=15)
    plot_group_bars(col2, option, df)

if nav == 'Histograms':
    col = st.sidebar.selectbox('Select a parameter', ls_product_num)
    option = st.sidebar.selectbox('Use Log', (False, True))
    # number = st.sidebar.number_input('Enter Percentile', step=15)
    plot_hist(col, option, 0.95, df)

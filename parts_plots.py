import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plost
import plotly.express as px

plt.rcParams['figure.figsize'] = [10, 5]
plt.style.use('fivethirtyeight')


df = pd.read_csv('basic_parts_data2.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title='Car Parts Dashboard')

ls_product_cat = ['Type', 'Subtype', 'Seller Name', 'Package', 'Condition', 'Make', 'Location', 'Region']
ls_product_num = ['Price', 'Inquires', 'Listing Duration', 'Moderated Duration', 'Views']


def home_page():
    # st.set_page_config(layout='wide')
    st.header('Car parts stats')

    pie_chart1 = px.pie(df,
                        title='Product Condition',
                        values=df['Condition'].value_counts(),
                        names=df['Condition'].value_counts().keys()
                        )

    cols = df.columns.tolist()

    a1, a2 = st.columns(2)
    b1, b2 = st.columns(2)
    c1, c2 = st.columns(2)
    a1.metric('Total Products', df['Product Id'].nunique())
    a2.metric('Top Product', df['Type'].value_counts().idxmax())

    b1.metric('Number of sellers', df['Seller Name'].nunique())
    b2.metric('Top Seller', df['Seller Name'].value_counts().idxmax())

    c1.metric('Number of Locations', df['Location'].nunique())
    c2.metric('Top Location', df['Location'].value_counts().idxmax())

    col_selection = st.multiselect('Fields', cols,
                                   default=['Title', 'Type', 'Seller Name', 'Location', 'Price', 'Make'])
    st.dataframe(df[col_selection])
    st.plotly_chart(pie_chart1)


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


nav = st.sidebar.radio('Select Plots', ('Home', 'Bars', 'Histograms'))

if nav=='Home':
    home_page()

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

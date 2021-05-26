import streamlit as st
import scipy
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.title('Food Demand Forecasting — Analytics Vidhya')


data_load_state = st.text('Loading data...')
weekly_data = pd.read_csv(r'C:\Users\Benny Antony\Downloads\Train.csv\Train.csv', nrows=1000)
center_info_data = pd.read_csv(r'C:\Users\Benny Antony\Downloads\fulfilment_center_info.csv',nrows=1000)
meal_data = pd.read_csv(r'C:\Users\Benny Antony\Downloads\meal_info.csv',nrows=1000)
st.subheader('Weekly Demand Data')
st.write(weekly_data)
#Bar Chart
st.bar_chart(weekly_data['num_orders'])
df = pd.DataFrame(weekly_data[:200], columns = ['num_orders','checkout_price','base_price'])
df.hist()
plt.show()
st.pyplot()
st.subheader('line')
st.line_chart(df)
chart_data = pd.DataFrame(weekly_data[:40], columns=['num_orders', 'base_price'])
st.area_chart(chart_data)
st.subheader('Fulfillment Center Information')
if st.checkbox('Show Center Information data'):
    st.subheader('Center Information data')
    st.write(center_info_data)
st.bar_chart(center_info_data['region_code'])
st.bar_chart(center_info_data['center_type'])
hist_data = [center_info_data['center_id'],center_info_data['region_code']]
group_labels = ['Center Id', 'Region Code']
fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 25])
st.plotly_chart(fig, use_container_width=True)
st.subheader('Meal Information')
st.write(meal_data)
st.bar_chart(meal_data['cuisine'])
agree = st.button('Click to see Categories of Meal')
if agree:
 st.bar_chart(meal_data['category'])


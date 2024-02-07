import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import plotly.express as px
import plotly.figure_factory as ff



#Altair Scatter plot
st.header("1. Altair Scatter plot")
chart_data = pd.DataFrame(np.random.randn(500,5), columns = ['a','b','c','d','e'])

chart = alt.Chart(chart_data).mark_circle().encode(x ='a', y='b', size = 'c', tooltip = ['a','b','c','d','e'])

st.altair_chart(chart)

#Interactive Line chats
st.header('2. Interactive charts')

st.subheader('2.1: Line chart')
df = pd.read_csv('C:\\Users\\ROHIT\\Downloads\\lang_data.csv')
lang_list = df.columns.tolist()
lang_choices = st.multiselect('Choose your language',lang_list)
new_df = df[lang_choices]
st.line_chart(new_df)

#Area chart
st.subheader('2.2: Area Chart')
st.area_chart(new_df)

#Data Visualization with Plotly
# import plotly.express as pe
# import plotly.figure_factory as ff
st.subheader('3.1 Displaying the dataset ')
df = pd.read_csv('C:\\Users\\ROHIT\\Downloads\\tips.csv')
st.dataframe(df.head())

st.subheader('3.2 Pie Chart')
fig = px.pie(df, values = 'total_bill', names = 'day')
st.plotly_chart(fig)


st.subheader('3.2 Pie Chart With Multiple Parametes')
fig = px.pie(df, values = 'total_bill', names = 'day',opacity = .7, color_discrete_sequence = px.colors.sequential.RdBu)
st.plotly_chart(fig)


#Histogram
st.subheader('3.4: Histogram')
x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)

hist_data = [x1,x2,x3]
group_label = ['Group-1','Group-2','Group-3']

fig = ff.create_distplot(hist_data, group_label, bin_size = [.1,.25,.5])
st.plotly_chart(fig)

import streamlit as st


st.title("Nigeria Farmland Analysis")


import pandas as pd
import plotly.express as px


farmland = pd.read_csv("farmlands.csv")


# Display the distribution of farm types
farm_type_distribution = farmland['type'].value_counts().reset_index()

fig1 = px.bar(farm_type_distribution, 'index', 'type', 
        labels={'index': '<b>Farm Type</b>', 'type':'<b>Counts</b>'},
        title='<b>Distribution of Farm Types</b>', width=700)
with st.expander('Farm Type Distribution', True):
    st.plotly_chart(fig1, use_container_width=True)
    if st.checkbox('Show raw data'):
        st.write(farm_type_distribution)
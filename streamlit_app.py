import streamlit as st

# Setting page size and title
st.set_page_config(layout="wide", page_title='NOVOTERN PORTFOLIO', page_icon='logo.png' ) 

st.title("Nigeria Farmland Analysis")

import pandas as pd
import plotly.express as px


farmland = pd.read_csv("farmlands.csv")


# Display the distribution of farm types
farm_type_distribution = farmland['type'].value_counts().reset_index()

# Calculate the farm categories
farms_by_category = farmland['category'].value_counts().reset_index(name='counts')

fig1 = px.bar(farm_type_distribution, 'type', 'count', text_auto=True,
        labels={'type': '<b>Farm Type</b>', 'count':'<b>Counts</b>'},
        title='<b>Distribution of Farm Types</b>', width=700)
with st.expander('Farm Type Distribution', True):
    st.plotly_chart(fig1, use_container_width=True)
    if st.checkbox('Show raw data', key=1):
        st.write(farm_type_distribution)
        
fig2 = px.pie(farms_by_category, 'category', 'counts', title='<b>Distribution of Farm Category</b>')
with st.expander('Distribution of Farm Category', True):
    st.plotly_chart(fig2, use_container_width=True)
    if st.checkbox('Show raw data', key=2):
        st.write(farms_by_category)
        
        
st.sidebar.subheader("Address")
st.sidebar.text("""
                The Philippi Centre, Oluwalogbon House, 
                Plot A Obafemi Awolowo Way, Alausa, 
                Ikeja, Lagos, Nigeria.
                """)
st.sidebar.subheader("Contact")
st.sidebar.text(
"""
+2347061228930 
+447831813568 
info@novotern.com
"""
)
st.sidebar.markdown("""
                    ## Quick Links
                    [Our Team](https://www.novotern.com/about/)
                    [Programs](https://paystack.shop/novotern)
                    [Careers](https://www.novotern.com/#)
                    [Partnership](https://www.novotern.com/contact/)                
                    """)

st.sidebar.markdown("[LinkedIn](https://www.novotern.com/)") 
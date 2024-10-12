import streamlit as  st 
import pandas as pd
import numpy as np
import plotly.express as px
import time


# read data
df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/refs/heads/master/bank.csv")

# page config and seo 
st.set_page_config(
    
    # for SEO
    page_title = '(simulation)Real-time Bank Data Dashboard',
    page_icon = "📊",
    layout = 'wide',
    
)


 # '''Title for webpage dashboard'''

st.title("Simulation of Real-time Bank Data Dashboard")


# ''' top-level filters section'''

# st.sidebar.selectbox for filter as a side column, while st.selectbox for horizontal filter'''

job_filter = st.selectbox("Select the job", pd.unique(df['job']))

# replacing current elements  (like picttures for video)
# by creating an empty container for exact same place

placeholder = st.empty()

# ''' data-frame filter'''

df = df[df['job'] == job_filter]

for seconds in range(200): # for deploying , while True: to refresh all the time
    df['age_new'] = df['age'] * np.random.choice(range(1,5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1,5))


    # kpi section (key performance indicators)

    # creating kpi's

    avg_age = np.mean(df['age_new'])
    count_married = int(df[(df['marital'] == 'married')]['marital'].count() + np.random.choice(range(1,3)))
    balance = np.mean(df['balance_new'])

    # defining a container in placeholder and keeping components in it

    with placeholder.container():
        # create 3 columns 
        kpi1, kpi2, kpi3 = st.columns(3)
        
        # fill in these columns with
        kpi1.metric(label="Age (avg)", value=round(avg_age), delta = round(avg_age) - 10 )
        kpi2.metric(label="Married (count)", value=int(count_married), delta =  -10 + count_married)
        kpi3.metric(label="A/C Balance (avg)", value=f"$ {round(balance,2)}", delta = -round(balance/count_married)*100 )

        '''charts section'''

        # create 2 columns for charts

        fig1, fig2 = st.columns(2)
        with fig1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(data_frame = df,  x = 'age_new',  y = 'marital')
            st.write(fig)
            
        with fig2:
            st.markdown("### Second Chart")
            fig = px.histogram(data_frame = df , x = 'age_new')
            st.write(fig)
            

        # '''table section'''

        st.markdown("### Detailed Data view")

        # managing api calls per minute (for when use API with limits)
        st.dataframe(df)
        
    # Sleep to simulate real-time updates
    time.sleep(1) # to refresh every 0.5 or 1 or based on Api calls, data updates, refresh cycles etc.

# placeholder.empty() to clear the container
placeholder.empty() 

# caption

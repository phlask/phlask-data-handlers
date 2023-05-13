import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import pandas as pd
import plotly.express as px # interactive charts 
import numpy as np
import time

# Generate hashed passwords
hashed_passwords = stauth.Hasher(['abc123']).generate()

# Replace passwords in config.yaml with hashed_passwords
# We could automate this step if desired

# Load configuration file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create an authentication object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Create login widget
name, authentication_status, username = authenticator.login('Login', 'main')

# Handle authentication status
if authentication_status:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{name}*')
    df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")


    # st.set_page_config(
    #     page_title = 'Real-Time Data Science Dashboard',
    #     page_icon = '✅',
    #     layout = 'wide'
    # )

    # dashboard title

    st.title("Real-Time / Live Data Science Dashboard")

    # top-level filters 

    job_filter = st.selectbox("Select the Job", pd.unique(df['job']))


    # creating a single-element container.
    placeholder = st.empty()

    # dataframe filter 

    df = df[df['job']==job_filter]

    # near real-time / live feed simulation 

    for seconds in range(200):
    #while True: 
        
        df['age_new'] = df['age'] * np.random.choice(range(1,5))
        df['balance_new'] = df['balance'] * np.random.choice(range(1,5))

        # creating KPIs 
        avg_age = np.mean(df['age_new']) 

        count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))
        
        balance = np.mean(df['balance_new'])

        with placeholder.container():
            # create three columns
            kpi1, kpi2, kpi3 = st.columns(3)

            # fill in those three columns with respective metrics or KPIs 
            kpi1.metric(label="Age ⏳", value=round(avg_age), delta= round(avg_age) - 10)
            kpi2.metric(label="Married Count 💍", value= int(count_married), delta= - 10 + count_married)
            kpi3.metric(label="A/C Balance ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)

            # create two columns for charts 

            fig_col1, fig_col2 = st.columns(2)
            with fig_col1:
                st.markdown("### First Chart")
                fig = px.density_heatmap(data_frame=df, y = 'age_new', x = 'marital')
                st.write(fig)
            with fig_col2:
                st.markdown("### Second Chart")
                fig2 = px.histogram(data_frame = df, x = 'age_new')
                st.write(fig2)
            st.markdown("### Detailed Data View")
            st.dataframe(df)
            time.sleep(1)
        # st.title('Protected Content')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
    

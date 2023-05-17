import streamlit as st
import streamlit_authenticator as stauth # third party package for authentication
import yaml
from yaml.loader import SafeLoader
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the project root directory to the Python path
sys.path.append(project_root)

from admin.admin_classes import prodAdmin, betaAdmin, testAdmin

example_water_data = prodAdmin().getTap(prodAdmin().water_db_live, 1)

# Generate hashed passwords
hashed_passwords = stauth.Hasher(['abc123', 'def456']).generate()

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

name, authentication_status, username = authenticator.login("Phlask Admin Dashboard \n Enter your username and password to log in.", 'main')

if authentication_status:
    # Add a title
    st.sidebar.title("Phlask Admin Dashboard")
    st.sidebar.markdown("""
    Welcome to the Phlask Admin Dashboard! Here, you can interact with the 
    database in real-time. You can view, edit, and update the data directly 
    from this dashboard. This is a powerful tool that allows administrators 
    to manage the data in an easy and intuitive way.
    """)
    authenticator.logout('Logout', 'sidebar', key='unique_key')

    st.write(f'Example data from the database: {example_water_data}')

# Display error or warning messages
if authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

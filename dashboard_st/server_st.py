import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import pandas as pd
import json
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the project root directory to the Python path
sys.path.append(project_root)

from admin.admin_classes import prodAdmin, betaAdmin, testAdmin


def parse_and_filter_dicts(dict_list, keys):
    # Function to parse any stringified JSON objects and filter out unnecessary keys
    parsed_filtered_dict_list = []
    for record in dict_list:
        # Convert strings to JSON objects
        for key in record:
            if isinstance(record[key], str):
                try:
                    record[key] = json.loads(record[key])
                except json.JSONDecodeError:
                    pass  # If decoding fails, leave the value as it is

        # If 'hours' is an empty dict, 'nan', or NaN, remove it
        if 'hours' in record and (not record['hours'] or pd.isna(record['hours']) or record['hours'] == 'nan'):
            del record['hours']

        # Filter out unnecessary keys
        filtered_dict = {key: record[key] for key in keys if key in record}
        parsed_filtered_dict_list.append(filtered_dict)

    return parsed_filtered_dict_list





# List of allowed keys in your Firebase database schema for the create_dataframe() function
allowed_keys = [
    'access', 'address', 'city', 'description', 'filtration',
    'gp_id', 'handicap','hours', 'lat', 'lon', 'norms_rules', 'organization', 
    'phone', 'quality', 'service', 'statement', 'tap_type', 'tapnum', 
    'vessel', 'zip_code', 
]

# This function oposed to the one below is for the original data set and only allows data with the keys stored inside the function. Hence the req in the name.

# def create_dataframe_req(data_list):
#     records = []
#     for item in data_list:
#         try:
#             record = {
#                 'access': item['access'],
#                 'address': item['address'],
#                 'city': item['city'],
#                 'description': item['description'],
#                 'filtration': item['filtration'],
#                 'gp_id': item['gp_id'],
#                 'handicap': item['handicap'],
#                 'hours': item['hours'],
#                 'lat': item['lat'],
#                 'lon': item['lon'],
#                 'norms_rules': item['norms_rules'],
#                 'organization': item['organization'],
#                 'permanently_closed': item['permanently_closed'],
#                 'phone': item['phone'],
#                 'quality': item['quality'],
#                 'service': item['service'],
#                 'statement': item['statement'],
#                 'status': item['status'],
#                 'tap_type': item['tap_type'],
#                 'tapnum': item['tapnum'],
#                 'vessel': item['vessel'],
#                 'zip_code': item['zip_code']
#             }
#             records.append(record)
#         except:
#             pass

    
#     df = pd.DataFrame(records)
#     return df


# This function allows all of the data that is present in our firebase database. It is more flexible than the one above but it is also more prone to errors.
# With the use of the allowed_keys list above we can filter out the data so that when we use the update button we don't get any errors and the data is updated correctly.
def create_dataframe(data_list):
    records = []
    all_keys = set()
    
    # Collect all keys from the dictionaries
    for item in data_list:
        keys = set(item.keys())
        all_keys.update(keys)
    
    # Create a record for each item, extracting specific data and storing additional keys
    for item in data_list:
        record = {}
        if 'access' in item:
            record['access'] = item['access']
        if 'address' in item:
            record['address'] = item['address']
        if 'city' in item:
            record['city'] = item['city']
        if 'description' in item:
            record['description'] = item['description']
        if 'filtration' in item:
            record['filtration'] = item['filtration']
        if 'gp_id' in item:
            record['gp_id'] = item['gp_id']
        if 'handicap' in item:
            record['handicap'] = item['handicap']
        if 'hours' in item:
            record['hours'] = str(item['hours'])
            print(type(record['hours']))
        if 'lat' in item:
            record['lat'] = item['lat']
        if 'lon' in item:
            record['lon'] = item['lon']
        if 'norms_rules' in item:
            record['norms_rules'] = item['norms_rules']
        if 'organization' in item:
            record['organization'] = item['organization']
        if 'permanently_closed' in item:
            record['permanently_closed'] = item['permanently_closed']
        if 'phone' in item:
            record['phone'] = item['phone']
        if 'quality' in item:
            record['quality'] = item['quality']
        if 'service' in item:
            record['service'] = item['service']
        if 'statement' in item:
            record['statement'] = item['statement']
        if 'status' in item:
            record['status'] = item['status']
        if 'tap_type' in item:
            record['tap_type'] = item['tap_type']
        if 'tapnum' in item:
            record['tapnum'] = item['tapnum']
        if 'vessel' in item:
            record['vessel'] = item['vessel']
        if 'zip_code' in item:
            record['zip_code'] = item['zip_code']


        # Add more specific data extraction as needed
        
        # Store additional keys and values
        for key, value in item.items():
            if key not in record:
                record[key] = value
        
        records.append(record)
    
    df = pd.DataFrame(records)
    return df



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
# Create login widget
name, authentication_status, username = authenticator.login(" Phlask Admin Dashboard \n Enter your username and password to log in.", 'main')

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
    if st.sidebar.button('Switch Accoutns'):
        st.stop()

    # Main content
    water_data = prodAdmin().getDb(prodAdmin().water_db_live)
    df = create_dataframe(water_data)

    edited_df = st.experimental_data_editor(df, height=500, width=1000)
    edited_df = edited_df.dropna(subset=['tapnum'])
    edited_df['tapnum'] = edited_df['tapnum'].astype(int)

    # Add a button to send the data back to Firebase
    if st.button('Update Firebase'):
        # Replace NaN values in 'hours' with empty dictionary
        edited_df['hours'] = edited_df['hours'].apply(lambda x: {} if pd.isna(x) else x)

        # Convert the DataFrame back to a list of dictionaries
        updated_data = edited_df.to_dict('records')
        filtered_data = parse_and_filter_dicts(updated_data, allowed_keys)

        prodAdmin().updateDb(prodAdmin().water_db_live, filtered_data)

    # Display error or warning messages
    if authentication_status is False:
        st.error('Username/password is incorrect')
    elif authentication_status is None:
        st.warning('Please enter your username and password')
    
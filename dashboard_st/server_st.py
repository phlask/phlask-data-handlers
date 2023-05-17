import streamlit as st
import streamlit_authenticator as stauth # third party package for authentication
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
allowed_water_keys = [
    'access', 'address', 'city', 'description', 'filtration',
    'gp_id', 'handicap','hours', 'lat', 'lon', 'norms_rules', 'organization', 
    'phone', 'quality', 'service', 'statement', 'tap_type', 'tapnum', 
    'vessel', 'zip_code', 
]

def create_water_dataframe(data_list):
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

# List of allowed keys in your Firebase database schema for the create_dataframe() function
allowed_food_keys = [ 'access', 'address', 'city', 'days_open', 'description', 'handicap', 'hours', 'id_required', 'kid_only', 'lat', 'lon', 'organization', 'time_open', 'url', 'zip_code']

def create_food_dataframe(data_list):
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
        if 'days_open' in item:
            record['days_open'] = item['days_open']
        if 'description' in item:
            record['description'] = item['description']
        if 'handicap' in item:
            record['handicap'] = item['handicap']
        if 'hours' in item:
            record['hours'] = str(item['hours'])
            print(type(record['hours']))
        if 'id_required' in item:
            record['id_required'] = item['id_required']
        if 'kid_only' in item:
            record['kid_only'] = item['kid_only']
        if 'lat' in item:
            record['lat'] = item['lat']
        if 'lon' in item:
            record['lon'] = item['lon']
        if 'organization' in item:
            record['organization'] = item['organization']
        if 'time_open' in item:
            record['time_open'] = item['time_open']
        if 'url' in item:
            record['url'] = item['url']
        if 'zip_code' in item:
            record['zip_code'] = item['zip_code']
        
        # Store additional keys and values
        for key, value in item.items():
            if key not in record:
                record[key] = value
        
        records.append(record)
    
    df = pd.DataFrame(records)
    return df

# Define a mapping for each resource to its allowed keys
resource_allowed_keys_and_df_func_map = {
    "water": {
        "allowed_keys": allowed_water_keys,
        "create_dataframe": create_water_dataframe
    },
    "food": {
        "allowed_keys": allowed_food_keys,  # list of allowed keys for 'food'
        "create_dataframe": create_food_dataframe  # function to create a dataframe for 'food'
    },
    # add more mappings as needed
}

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

# Define a mapping for resource to database and "tapnum" replacement
resource_db_map = {
    "water": {"live": "water_db_live", "verify": "water_db_verify", "tapnum": "tapnum"},
    "food": {"live": "food_db_live", "verify": "food_db_verify", "tapnum": "foodnum"},
    "forage": {"live": "forage_db_live", "verify": "forage_db_verify", "tapnum": "foragenum"},
    # add more mappings as needed
}


# Define a mapping for production level to admin object
prod_level_admin_map = {
    "prod": prodAdmin,
    "beta": betaAdmin,
    "test": testAdmin,
}

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

    # Add selection for resources
    resources = ['water', 'food', 'forage']  # Add or remove resources as needed
    selected_resource = st.sidebar.selectbox('Select a resource:', resources)

    # Add selection for production level
    prod_levels = ['prod', 'beta', 'test']  # Add or remove production levels as needed
    selected_prod_level = st.sidebar.selectbox('Select a production level:', prod_levels)

    # Add selection for live/verify database
    db_type = ['live', 'verify']  # Add or remove resources as needed
    selected_db_type = st.sidebar.selectbox('Select a database type:', db_type)

    # Create an object based on the selected production level
    admin_obj = prod_level_admin_map.get(selected_prod_level, lambda: st.error('Invalid production level selected'))()

    # Get the data based on the selected resource and database type
    db_attribute = resource_db_map.get(selected_resource, {}).get(selected_db_type)
    if db_attribute is not None:
        data = admin_obj.getDb(getattr(admin_obj, db_attribute))
    else:
        st.error('Invalid resource or database type selected')
    
    allowed_keys = resource_allowed_keys_and_df_func_map.get(selected_resource, {}).get("allowed_keys")
    create_dataframe = resource_allowed_keys_and_df_func_map.get(selected_resource, {}).get("create_dataframe")

    if allowed_keys is None or create_dataframe is None:
        st.error('Invalid resource selected')


    df = create_dataframe(data)

    edited_df = st.experimental_data_editor(df, height=500, width=1000)

    # Handle the tapnum replacement dynamically
    tapnum_replacement = resource_db_map.get(selected_resource, {}).get("tapnum", "tapnum")
    edited_df = edited_df.dropna(subset=[tapnum_replacement])
    edited_df[tapnum_replacement] = edited_df[tapnum_replacement].astype(int)

    # Add a button to send the data back to Firebase
    if st.button('Update Firebase'):
        # Replace NaN values in 'hours' with empty dictionary
        edited_df['hours'] = edited_df['hours'].apply(lambda x: {} if pd.isna(x) else x)

        # Convert the DataFrame back to a list of dictionaries
        updated_data = edited_df.to_dict('records')
        filtered_data = parse_and_filter_dicts(updated_data, allowed_keys)

        admin_obj.updateDb(getattr(admin_obj, db_attribute), filtered_data)

    # Display error or warning messages
    if authentication_status is False:
        st.error('Username/password is incorrect')
    elif authentication_status is None:
        st.warning('Please enter your username and password')

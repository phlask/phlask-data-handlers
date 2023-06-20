import sys
import os
import yaml
from yaml.loader import SafeLoader
import json
import pandas as pd
import streamlit as st
from dataclasses import dataclass
MAPBOX_API_KEY = os.environ.get('MAPBOX_API_KEY')
st.set_page_config(page_title="Phlask Admin Dashboard", page_icon=":earth_americas:", layout="centered")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the project root directory to the Python path using insert() at position -1 
sys.path.insert(-1, PROJECT_ROOT)

from admin.admin_classes import prodAdmin, betaAdmin, testAdmin

# Define a mapping for resource to database and "tapnum" replacement
RESOURCE_DB_MAP = {
    "water": {"live": "water_db_live", "verify": "water_db_verify", "tapnum": "tapnum"},
    "food": {"live": "food_db_live", "verify": "food_db_verify", "tapnum": "foodnum"},
    "forage": {"live": "forage_db_live", "verify": "forage_db_verify", "tapnum": "foragenum"},
    # add more mappings as needed
}

# Define a mapping for production level to admin object
PROD_ADMIN_MAP = {
    "prod": prodAdmin,
    "beta": betaAdmin,
    "test": testAdmin,
}

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
        if 'hours' in record and (
            (isinstance(record['hours'], dict) and not record['hours']) or
            (isinstance(record['hours'], str) and (not record['hours'] or record['hours'] == 'nan'))
        ):
            del record['hours']

        # Filter out unnecessary keys
        filtered_dict = {key: record[key] for key in keys if key in record}
        parsed_filtered_dict_list.append(filtered_dict)

    return parsed_filtered_dict_list


@dataclass
class Resource:
    allowed_keys: list

    def create_dataframe(self, data_list):
        if data_list is None:
            return pd.DataFrame()  # return an empty DataFrame

        records = []
        for item in data_list:
            if item is not None:
                record = {key: item.get(key) for key in self.allowed_keys if key in item}

                # Convert 'hours' value to string if it's a list of dictionaries
                if 'hours' in record and isinstance(record['hours'], list):
                    try:
                        record['hours'] = json.dumps(record['hours'])
                    except:
                        pass  # If encoding fails, leave the value as it is

                records.append(record)

        return pd.DataFrame(records)

# Define allowed keys for each resource
allowed_water_keys = [
    'access', 'address', 'city', 'description', 'filtration',
    'gp_id', 'handicap', 'hours', 'lat', 'lon', 'norms_rules', 'organization',
    'phone', 'quality', 'service', 'statement', 'tap_type', 'tapnum',
    'vessel', 'zip_code',
]

allowed_food_keys = [
    'access', 'address', 'city', 'days_open', 'description', 'handicap', 'hours',
    'id_required', 'kid_only', 'lat', 'lon', 'organization', 'time_open', 'url', 'zip_code'
]

# Define allowed keys for 'forage'
allowed_forage_keys = [
    'city', 'common_name', 'genus', 'planting_site_id', 'point_x', 'point_y', 
    'postal_code', 'species', 'street_address', 'tree_id', 'updated_at']

# Instantiate Resource objects
water_resource = Resource(allowed_water_keys)
food_resource = Resource(allowed_food_keys)
forage_resource = Resource(allowed_forage_keys)  # Forage resource object

# Define a mapping for each resource to its object
resource_map = {
    "water": water_resource,
    "food": food_resource,
    "forage": forage_resource,  # Add forage resource to map
}

#-----> STREAMLIT APP <-----#
# Add a title
st.sidebar.title("Phlask Admin Dashboard")
st.sidebar.markdown("""
Welcome to the Phlask Admin Dashboard! Here, you can interact with the 
database in real-time. You can view, edit, and update the data directly 
from this dashboard. This is a powerful tool that allows administrators 
to manage the data in an easy and intuitive way.
""")

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
admin_obj = PROD_ADMIN_MAP.get(selected_prod_level, lambda: st.error('Invalid production level selected'))()

# Get the data based on the selected resource and database type
db_attribute = RESOURCE_DB_MAP.get(selected_resource, {}).get(selected_db_type)
if db_attribute is not None:
    data = admin_obj.getDb(getattr(admin_obj, db_attribute))
else:
    st.error('Invalid resource or database type selected')

resource_obj = resource_map.get(selected_resource)

if resource_obj is None:
    st.error('Invalid resource selected')

df = resource_obj.create_dataframe(data)

edited_df = st.data_editor(df, height=500, width=1000, key="data_editor")
st.write("Here's the session state:")
st.write(st.session_state["data_editor"])

# Handle the tapnum replacement dynamically
tapnum_replacement = RESOURCE_DB_MAP.get(selected_resource, {}).get("tapnum", "tapnum")
if tapnum_replacement in edited_df.columns:
    edited_df = edited_df.dropna(subset=[tapnum_replacement])
    edited_df[tapnum_replacement] = edited_df[tapnum_replacement].astype(int)

# Add a button to send the data back to Firebase
if st.button('Update Firebase'):
    # Replace NaN values in 'hours' with empty dictionary
    edited_df['hours'] = edited_df['hours'].apply(lambda x: {} if pd.isna(x) else x)

    # Convert the DataFrame back to a list of dictionaries
    updated_data = edited_df.to_dict('records')
    filtered_data = parse_and_filter_dicts(updated_data, resource_obj.allowed_keys)

    admin_obj.updateDb(getattr(admin_obj, db_attribute), filtered_data)


#-----> ANALYTICS PORTION <-----#
# import pydeck as pdk

# assert 'lat' in df and 'lon' in df, "DataFrame should have 'lat' and 'lon' columns"
# df = df.dropna(subset=['lat', 'lon'])
# df = df[(df['lat'] != '') & (df['lon'] != '')]

# st.header("Resource Density Map")
# # Convert 'lat' and 'lon' to float
# df['lat'] = df['lat'].astype(float)
# df['lon'] = df['lon'].astype(float)

# # Drop all other columns except 'lat' and 'lon'
# df = df[['lat', 'lon']]

# st.pydeck_chart(pdk.Deck(
#     map_style=None,
#     initial_view_state=pdk.ViewState(
#         latitude=df['lat'].mean(),
#         longitude=df['lon'].mean(),
#         zoom=11,
#         pitch=50,
#     ),
#     layers=[
#         pdk.Layer(
#             'HexagonLayer',
#             data=df,
#             get_position='[lon, lat]',
#             radius=200,
#             elevation_scale=4,
#             elevation_range=[0, 1000],
#             pickable=True,
#             extruded=True,
#         ),
#         pdk.Layer(
#             'ScatterplotLayer',
#             data=df,
#             get_position='[lon, lat]',
#             get_color='[200, 30, 0, 160]',
#             get_radius=200,
#         ),
#     ],
# ))


import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the project root directory to the Python path
sys.path.append(project_root)
from admin  import admin_classes as admin


import requests
def format_address(address_pattern):
    # Split the address pattern into its parts
    parts = address_pattern.split(',')
    
    # Remove any leading or trailing whitespace from each part
    parts = [part.strip() for part in parts]
    
    # If the address pattern doesn't have a state, add it as the second-to-last part
    if len(parts) < 3:
        parts.insert(-1, 'Pennsylvania')
    
    # Add the country as "United States"
    parts.append('United States')
    
    # Join the parts into a formatted string
    formatted_address = ', '.join(parts)
    
    return formatted_address



def water_croudsource(address, ref):
    taps = admin.prodAdmin.getDb(ref)
    try:
        for tap in taps:
            try:
                if tap['address'] == address:
                    return tap
            except:
                pass
    except:
        pass
# print(prodAdmin().water_db_live)
print(type(water_croudsource("Wishbone, South 13th Street, Philadelphia, PA, USA", admin.prodAdmin().water_db_live)))

# import the necessary libraries

data =  water_croudsource("Wishbone, South 13th Street, Philadelphia, PA, USA", admin.prodAdmin().water_db_verify)

# define a function to clean the data
def cleanup_water_data(uncleaned_data):
    root=admin.prodAdmin.getCount(admin.prodAdmin().water_db_live)
    cleaned_data = {root: {}}
    # copy over the fields that don't need to be cleaned
    cleaned_data[root]["access"]=uncleaned_data["access"]
    cleaned_data[root]["address"]=uncleaned_data["address"]
    cleaned_data[root]["description"]=uncleaned_data["description"]
    cleaned_data[root]["filtration"]=uncleaned_data["filtration"]
    cleaned_data[root]["handicap"]=uncleaned_data["handicap"]
    #  change organization to name and vice versa 
    cleaned_data[root]['organization'] = uncleaned_data['name']
    cleaned_data[root]['service'] = uncleaned_data['service']
    cleaned_data[root]['statement'] = uncleaned_data['statement']
    cleaned_data[root]['tap_type'] = uncleaned_data['tap_type']
    cleaned_data[root]['vessel'] = uncleaned_data['vessel']
    cleaned_data[root]['norms_rules'] = uncleaned_data['norms_rules']

    match cleaned_data[root]["filtration"]:
        case False:
            cleaned_data[root]["filtration"]="No"
        case True:
            cleaned_data[root]["filtration"]="Yes"
    match cleaned_data[root]["vessel"]:
        case False:
            cleaned_data[root]["vessel"]="No"
        case True:
            cleaned_data[root]["vessel"]="Yes"
    match cleaned_data[root]["handicap"]:
        case False:
            cleaned_data[root]["handicap"]="No"
        case True: 
            cleaned_data[root]["handicap"]="Yes"
    # Define the API endpoint and API key
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    api_key = 'AIzaSyDCiiL2U0bnAk_K8sh2_FpTznavP9PQgEs'

    # Define the address pattern you want to geocode

    # Format the address pattern for the API call
    formatted_address = format_address(cleaned_data[root]["address"])

    # Send the API request
    response = requests.get(url, params={'address': formatted_address, 'key': api_key})

    # Print the latitude and longitude of the first result
    result = response.json()['results'][0]
    cleaned_data[root]['lat'] = result['geometry']['location']['lat']
    cleaned_data[root]['lon'] = result['geometry']['location']['lng']
    cleaned_data[root]['gp_id'] = result["place_id"]
    cleaned_data[root]['tapnum'] = root
    
    
    
    
    # set some default values for fields that aren't present in the uncleaned data
    cleaned_data[root]['permanetley_closed'] = False
    cleaned_data[root]['quality'] = ""
    cleaned_data[root]['status'] = ""
    cleaned_data[root]['phone'] = ""
    
    return cleaned_data

results=(cleanup_water_data(data))
print(results)

admin.prodAdmin().water_db_live.update(results)

##FILTERATION IS MISPELLED IN THE FIREBASE DB
import firebase_admin
from firebase_admin import credentials, db
import requests
import json
from collections import defaultdict
import logging
# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

resource_counts = defaultdict(int)


slack_webhook_url = 'slack_webhook_url'

def send_slack_message(message):
    payload = {'text': message}
    headers = {'content-type': 'application/json'}
    response = requests.post(slack_webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        raise ValueError('Request to Slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))

def get_key(data):
    print(data)
    if isinstance(data, list):
        # If data is a list, return the index of the first item
        return 0
    elif isinstance(data, dict):
        # If data is a dict, return the first key
        for key in data.keys():
            return key

def handle_event(event, db_name):
    event_type = event.event_type
    data_info = event.data
    try:
        if event_type == 'put':
            if isinstance(data_info, list):
                for node in data_info:
                    process_node(node, db_name)
            elif isinstance(data_info, dict):
                process_node(data_info, db_name)
            logging.info(f'{db_name}: {resource_counts[db_name]} taps added.')
    except Exception as e:
        print(f"An error occurred while processing the {db_name} database event: {e}")

def process_node(node, db_name):
    root = get_key(node)
    organization = node.get("name")
    address = node.get("address")
    description = node.get("description")
    resource_counts[db_name] += 1  # Increment the count for the resource type
    message = f"A new tap has been added to the *{db_name} verify* database! \n Here's some quick info about it: \n"
    if organization:
        message += f"\n*Organization:* {organization}"
    if description:
        message += f"\n*Description:* {description}"
    if address:
        message += f"\n*Address:* {address}"
    message += f"\n\nYou can view the tap here: https://phlask.me once it's been verified :phlask-water: :white_check_mark:"
    send_slack_message(message)


apps = [
    {
        'name': 'water-verify',
        'credentials': credentials.Certificate('phlask.json'),
        'databaseURL': 'https://phlask-web-map-prod-water-verify.firebaseio.com/'
    },
    {
        'name': 'food-verify',
        'credentials': credentials.Certificate('phlask.json'),
        'databaseURL': 'https://phlask-web-map-prod-food-verify.firebaseio.com/'
    },
    {
        'name': 'forage-verify',
        'credentials': credentials.Certificate('phlask.json'),
        'databaseURL': 'https://phlask-web-map-prod-foraging-verify.firebaseio.com/'
    },
    {
        'name': 'bathroom-verify',
        'credentials': credentials.Certificate('phlask.json'),
        'databaseURL': 'https://phlask-web-map-prod-bathroom-verify.firebaseio.com/'
    },
]

# Initialize the apps with unique names
# Initialize the apps with unique names and start listening to updates
for app_config in apps:
    app = firebase_admin.initialize_app(app_config['credentials'], {
        'databaseURL': app_config['databaseURL']
    }, name=app_config['name'])

    ref = db.reference('/', app=app)
    db_name = app_config['databaseURL'].split('//')[-1].split('-')[4]
    ref.listen(lambda event, db_name=db_name: handle_event(event, db_name))


import firebase_admin
from firebase_admin import credentials, db

apps = [
    {
        'name': 'water-verify',
        'databaseURL': 'https://phlask-web-map-prod-water-verify.firebaseio.com/'
    },
    # {
    #     'name': 'food-verify',
    #     'databaseURL': 'https://phlask-web-map-prod-food-verify.firebaseio.com/'
    # },
    # {
    #     'name': 'forage-verify',
    #     'databaseURL': 'https://phlask-web-map-prod-foraging-verify.firebaseio.com/'
    # },
    # {
    #     'name': 'bathroom-verify',
    #     'databaseURL': 'https://phlask-web-map-prod-bathroom-verify.firebaseio.com/'
    # },
]

cred = credentials.Certificate('phlask.json')

def order_data(app_config):
    app = firebase_admin.initialize_app(cred, {
        'databaseURL': app_config['databaseURL']
    }, name=app_config['name'])

    ref = db.reference('/', app)
    data = ref.get()

    if data:
        data = [i for i in data if i]
        ref.delete()
        for i, item in enumerate(data):
            ref.child(str(i)).set(item)

    firebase_admin.delete_app(app)

for app_config in apps:
    order_data(app_config)

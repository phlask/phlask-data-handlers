from itertools import count
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred, { 'databaseURL': 'https://phlask-pyrebase-default-rtdb.firebaseio.com/' })


# Database References for the Beta and Prod DB
Prod_database = db.reference('Phlask')
Beta_database = db.reference('phlask-struct/phlask-web-map')
Test_database = db.reference('phlask-struct/phlask-web-map')


# Retrieves the nested data within the Beta DB
# Returns in the form of dictionaries in a list
def get_beta_db():
    beta_db = Beta_database.get()
    return beta_db
# print(type(get_beta_db()))

# Retrieves the nested data within the prod DB 
# Returns in the form of dictionaries in a list
def get_prod_db():
    prod_db = Prod_database.get()
    return prod_db

def listener(event):
    db.reference("https://phlask-pyrebase-default-rtdb.firebaseio.com/phlask-struct/phlask-web-map").set(False)

# If there is a change in the database, run the listener function
def listen_db():
    dbevent = Prod_database.listen(listener)
    return dbevent
# listen_db()

changed = Beta_database.get_if_changed("https://phlask-pyrebase-default-rtdb.firebaseio.com/Phlask")
# print(type(changed))
changedjson = changed[1]
#turn changed json into a dictionary
# print((changedjson[0]))

def update_db():
    count = 0
    for dict in changedjson:
        if dict["tapnum"] == count:
            count += 1
    print(count)
prod_data = get_prod_db()
beta_data = get_beta_db()

def delete_node():
    for node in Prod_database.get():
        Prod_database.child(node).delete()
# delete_node()

def upload_updated_data():
    count = 0
    for dict in beta_data:
        if dict["tapnum"] == count:
            Prod_database.update({count: dict})
            count += 1
            print(count)
# update_beta_data()

def update_beta_data2():
    count = 0
    if changedjson:
        for dict in changedjson:
            if dict["tapnum"] == count:
                Prod_database.update({count: dict})
                count += 1
                print(count)

update_beta_data2()
from itertools import count
from mimetypes import init
from weakref import ref
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Imports
#----------------------------------------------------------------------------------------------------------------------

cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred, { 'databaseURL': 'https://phlask-pyrebase-default-rtdb.firebaseio.com/' })
#Dummy Firebase RTDB and Creditentials
#----------------------------------------------------------------------------------------------------------------------
def get_db(ref):
    ref_db = ref.get()
    return ref_db
# EXAMPLE CALL (phlask_firebaseadmin): get_db(prod_water_db)
# takes the ref DB(prod) and returns a list of dictionaries of the data in the database (referring to the ref DB)
# this does not use any itereation reference and soley updates based of off how many nodes are in the DB.
#----------------------------------------------------------------------------------------------------------------------
# Under Work do not use yet
class ListenerClass:
    def __init__(self, ref):
        self.ref = ref

    def listener(self, event):
        ref.get()
# listen_db()
#----------------------------------------------------------------------------------------------------------------------
def get_changed_data(ref,url):
    changed = ref.get_if_changed(url)
    changed_dict_list = changed[1]
    return changed_dict_list
# EXAMPLE CALL (phlask_firebaseadmin): get_changed_data(prod_water_db, beta_water_url)
# takes the ref DB(prod) and alt_ref's url DB(beta) and returns the data in the alt_ref DB if it is different from the ref DB.
# Note this is different from the db_comparison() function which returns whether the ref DB and alt_ref DB are the same or not.
#----------------------------------------------------------------------------------------------------------------------
def db_dry_count(ref, url):
    changed=get_changed_data(ref,url)
    count = 0
    for dict in changed:
        if dict:
            count += 1
    print(count)
# EXAMPLE CALL (phlask_firebaseadmin): db_dry_count(prod_water_db, beta_water_url)
# takes the ref DB(prod) and alt_ref's url DB(beta) and prints a count of the nodes in the ref DB.
#----------------------------------------------------------------------------------------------------------------------
def db_comparison(ref, alt_ref):
    ref_data = get_db(ref)
    alt_ref_data = get_db(alt_ref)
    if ref_data == alt_ref_data:
        print("The databases are the same")
    else:
        print("The databases are not the same")
# EXAMPLE CALL (phlask_firebaseadmin): db_comparison(prod_water_db, beta_water_db)
# takes the ref DB(prod) and the alt_ref DB(beta) and prints whether the ref DB and alt_ref DB are the same or not.
#----------------------------------------------------------------------------------------------------------------------
def update_changed_db_iter(ref, url, iterate: str):
    changed=get_changed_data(ref,url)
    count = 0
    for dict in changed:
        if dict[iterate] == count:
            ref.update({count: dict})
            count += 1
            print(count)

# EXAMPLE CALL (phlask_firebaseadmin): update_changed_db(beta_water_db, beta_water_url)
# takes the ref DB(beta) and ref alterante DB(prod) and updates the ref DB with the data from the alt_ref DB.
# this does not use any itereation reference and soley updates based of off how many nodes are in the DB.
#----------------------------------------------------------------------------------------------------------------------
def update_changed_db(ref, url):
    changed=get_changed_data(ref,url)
    count = 0
    for dict in changed:
            ref.update({count: dict})
            count += 1
            print(count)

# EXAMPLE CALL (phlask_firebaseadmin): update_changed_db(beta_water_db, beta_water_url)
# takes the ref DB(beta) and ref alterante DB(prod) and updates the ref DB with the data from the alt_ref DB.
# this does not use any itereation reference and soley updates based of off how many nodes are in the DB.
#----------------------------------------------------------------------------------------------------------------------
def update_db(ref, alt_ref):
    alt_ref_data= get_db(alt_ref)
    count = 0
    for dict in alt_ref_data:
        ref.update({count: dict})
        count += 1
        print(count)

# EXAMPLE CALL (phlask_firebaseadmin): update_db(beta_water_db, beta_water_db)
# takes the ref DB(beta) and ref alterante DB(prod) and updates the ref DB with the data from the alt_ref DB.
# this does not use any itereation reference and soley updates based of off how many nodes are in the DB.
#----------------------------------------------------------------------------------------------------------------------
def update_db_iter(ref, alt_ref, iterate: str):
    alt_ref_data= get_db(alt_ref)
    count = 0
    for dict in alt_ref_data:
        if dict[iterate] == count:
            ref.update({count: dict})
            count += 1
            print(count)

# EXAMPLE CALL (phlask_firebaseadmin): update_db_iter(beta_water_db, beta_water_db, "tapnum")
# takes the ref DB(beta) and ref alterante DB(prod) and updates the ref DB with the data from the alt_ref DB.
# this iterates via tapnum in this example
#----------------------------------------------------------------------------------------------------------------------
def delete_node(ref):
    for node in ref.get():
        ref.child(node).delete()
        
# EXAMPLE CALL (phlask_firebaseadmin): delete_node(beta_water_db)
# deletes all nodes in the ref DB
#----------------------------------------------------------------------------------------------------------------------

# add new nodes to DB

def add_to_db(ref, data):
    ref.push(data)
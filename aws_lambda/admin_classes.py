import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import boto3
import json

s3 = boto3.resource('s3')

content_object = s3.Object('phlaskkey', 'phlask.json')
file_content = content_object.get()['Body'].read().decode('utf-8')
json_data = json.loads(file_content)
#----------------------------------------------------------------------------------------------------------------------
# Prod database URL's
pointer_url = "https://phlask-web-map-food-hours.firebaseio.com/"
prod_water_url_live = "https://phlask-web-map-prod-water-live.firebaseio.com/"
prod_water_url_verify = "https://phlask-web-map-prod-water-verify.firebaseio.com/"
prod_food_url_live = 'https://phlask-web-map-prod-food-live.firebaseio.com/'
prod_food_url_verify = 'https://phlask-web-map-food-hours.firebaseio.com/'
prod_forage_url_live = "https://phlask-web-map-prod-foraging-live.firebaseio.com/"
prod_forage_url_verify = 'https://phlask-web-map-prod-foraging-verify.firebaseio.com/'
prod_bathroom_url_live = "https://phlask-web-map-prod-bathroom-live.firebaseio.com/"
prod_bathroom_url_verify = "https://phlask-web-map-prod-bathroom-verify.firebaseio.com/"
#----------------------------------------------------------------------------------------------------------------------
# Beta database URL's 
beta_water_url_live = "https://phlask-web-map-beta-water-live.firebaseio.com/"
beta_water_url_verify = "https://phlask-web-map-beta-water-verify.firebaseio.com/"
beta_food_url_live = 'https://phlask-web-map-beta-food-live.firebaseio.com/'
beta_food_url_verify = 'https://phlask-web-map-beta-food-verify.firebaseio.com/'
beta_forage_url_live = "https://phlask-web-map-beta-foraging-live.firebaseio.com/"
beta_forage_url_verify = "https://phlask-web-map-beta-foraging-verify.firebaseio.com/"
beta_bathroom_url_live = "https://phlask-web-map-beta-bathroom-live.firebaseio.com/"
beta_bathroom_url_verify = "https://phlask-web-map-beta-bathroom-verify.firebaseio.com/"
#----------------------------------------------------------------------------------------------------------------------
# Test database URL's
test_water_url_live = "https://phlask-web-map-test-water-live.firebaseio.com/"
test_water_url_verify = "https://phlask-web-map-test-water-verify.firebaseio.com/"
test_food_url_live = 'https://phlask-web-map-test-food-live.firebaseio.com/'
test_food_url_verify = 'https://phlask-web-map-test-food-verify.firebaseio.com/'
test_forage_url_live = "https://phlask-web-map-test-foraging-live.firebaseio.com/"
test_forage_url_verify = "https://phlask-web-map-test-foraging-verify.firebaseio.com/"
test_bathroom_url_live = "https://phlask-web-map-test-bathroom-live.firebaseio.com/"
test_bathroom_url_verify = "https://phlask-web-map-test-bathroom-verify.firebaseio.com/"
#----------------------------------------------------------------------------------------------------------------------
#creds for initializing firebase admin

cred = credentials.Certificate(json_data)
firebase_admin.initialize_app(cred, { 'databaseURL': 'https://phlask-pyrebase-default-rtdb.firebaseio.com/' })
#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Prod DB's
pointer_init =  firebase_admin.initialize_app(cred, { 'databaseURL': pointer_url}, name="pointer_app")
prod_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': prod_water_url_live }, name="prod_water_live") #name is the app name
prod_food_live=firebase_admin.initialize_app(cred, { 'databaseURL': prod_food_url_live }, name="prod_food_live") #name is the app name
prod_forage_live=firebase_admin.initialize_app(cred, { 'databaseURL': prod_forage_url_live }, name="prod_forage_live") #name is the app name
prod_bathroom_live=firebase_admin.initialize_app(cred, { 'databaseURL': prod_bathroom_url_live }, name="prod_bathroom_live") #name is the app name
#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Beta DB's
beta_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': beta_water_url_live }, name="beta_water_live") #name is the app name
beta_food_live=firebase_admin.initialize_app(cred, { 'databaseURL': beta_food_url_live }, name="beta_food_live") #name is the app name
beta_forage_live=firebase_admin.initialize_app(cred, { 'databaseURL': beta_forage_url_live }, name="beta_forage_live") #name is the app name
beta_bathroom_live=firebase_admin.initialize_app(cred, { 'databaseURL': beta_bathroom_url_live }, name="beta_bathroom_live") #name is the app name
#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Test DB's
test_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': test_water_url_live }, name="test_water_live") #name is the app name
test_food_live=firebase_admin.initialize_app(cred, { 'databaseURL': test_food_url_live }, name="test_food_live") #name is the app name
test_forage_live=firebase_admin.initialize_app(cred, { 'databaseURL': test_forage_url_live }, name="test_forage_live") #name is the app name
test_bathroom_live=firebase_admin.initialize_app(cred, { 'databaseURL': test_bathroom_url_live }, name="test_bathroom_live") #name is the app name
#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the prod databases
prod_water_db_live = db.reference('/', app= prod_water_live)
prod_food_db_live = db.reference('/', app= prod_food_live)
prod_forage_db_live = db.reference('/', app= prod_forage_live)
prod_bathroom_db_live = db.reference('/', app= prod_bathroom_live)
#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the beta databases
beta_water_db_live = db.reference('/', app= beta_water_live)
beta_food_db_live = db.reference('/', app= beta_food_live)
beta_forage_db_live = db.reference('/', app= beta_forage_live)
beta_bathroom_db_live = db.reference('/', app= beta_bathroom_live)
#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the test databases
test_water_db_live = db.reference('/', app= test_water_live)
test_food_db_live = db.reference('/', app= test_food_live)
test_forage_db_live = db.reference('/', app= test_forage_live)
test_bathroom_db_live = db.reference('/', app= test_bathroom_live)
#----------------------------------------------------------------------------------------------------------------------
class prod_admin:
    def __init__(self):
        self.water_db_live = prod_water_db_live
        self.food_db_live = prod_food_db_live
        self.forage_db_live = prod_forage_db_live
        self.bathroom_db_live = prod_bathroom_db_live
    def get_db(ref):
        ref_db = ref.get()
        return ref_db
    def get_changed_data(ref,url):
        changed = ref.get_if_changed(url)
        changed_dict_list = changed[1]
        return changed_dict_list

    def db_dry_count(ref, url):
        changed=prod_admin.get_changed_data(ref,url)
        count = 0
        for dict in changed:
            if dict:
                count += 1
        print(count)
    def db_comparison(ref, alt_ref):
        ref_data = prod_admin.get_db(ref)
        alt_ref_data = prod_admin.get_db(alt_ref)
        if ref_data == alt_ref_data:
            print("The databases are the same")
        else:
            print("The databases are not the same")
    def update_changed_db_iter(ref, url, iterate: str):
        changed=prod_admin.get_changed_data(ref,url)
        count = 0
        for dict in changed:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def update_changed_db(ref, url):
        changed=prod_admin.get_changed_data(ref,url)
        count = 0
        for dict in changed:
            ref.update({count: dict})
            count += 1
            print(count)
    def update_db(ref, alt_ref):
        alt_ref_data= prod_admin.get_db(alt_ref)
        count = 0
        for dict in alt_ref_data:
            ref.update({count: dict})
            count += 1
            print(count)
    def update_db_iter(ref, alt_ref, iterate: str):
        alt_ref_data= prod_admin.get_db(alt_ref)
        count = 0
        for dict in alt_ref_data:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def delete_node(ref):
        for node in ref.get():
            ref.child(node).delete()
    def add_to_db(ref, data):
        ref.push(data)


class beta_admin:
    def __init__(self):
        self.water_db_live = beta_water_db_live
        self.food_db_live = beta_food_db_live
        self.forage_db_live = beta_forage_db_live
        self.bathroom_db_live = beta_bathroom_db_live
    def get_db(ref):
        ref_db = ref.get()
        return ref_db
    def get_changed_data(ref,url):
        changed = ref.get_if_changed(url)
        changed_dict_list = changed[1]
        return changed_dict_list

    def db_dry_count(ref, url):
        changed=beta_admin.get_changed_data(ref,url)
        count = 0
        for dict in changed:
            if dict:
                count += 1
        print(count)
    def db_comparison(ref, alt_ref):
        ref_data = beta_admin.get_db(ref)
        alt_ref_data = beta_admin.get_db(alt_ref)
        if ref_data == alt_ref_data:
            print("The databases are the same")
        else:
            print("The databases are not the same")
    def update_changed_db_iter(ref, url, iterate: str):
        changed=beta_admin.get_changed_data(ref,url)
        count = 0
        for dict in changed:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def update_changed_db(ref, url):
        changed=beta_admin.get_changed_data(ref,url)
        count = 0
        for dict in changed:
            ref.update({count: dict})
            count += 1
            print(count)
    def update_db(ref, alt_ref):
        alt_ref_data= beta_admin.get_db(alt_ref)
        count = 0
        for dict in alt_ref_data:
            ref.update({count: dict})
            count += 1
            print(count)
    def update_db_iter(ref, alt_ref, iterate: str):
        alt_ref_data= beta_admin.get_db(alt_ref)
        count = 0
        for dict in alt_ref_data:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def delete_node(ref):
        for node in ref.get():
            ref.child(node).delete()
    def add_to_db(ref, data):
        ref.push(data)
    

class test_admin:
    def __init__(self):
        self.water_db_live = test_water_db_live
        self.food_db_live = test_food_db_live
        self.forage_db_live = test_forage_db_live
        self.bathroom_db_live = test_bathroom_db_live
    def get_db(self, ref):
        ref_db = ref.get()
        return ref_db
    def get_changed_data(ref,url):
        changed = ref.get_if_changed(url)
        changed_dict_list = changed[1]
        return changed_dict_list

    def db_dry_count(ref, url):
        changed=test_admin.get_changed_data(ref,url)
        count = 0
        for dict in changed:
            if dict:
                count += 1
        print(count)
    def db_comparison(ref, alt_ref):
        ref_data = test_admin.get_db(ref)
        alt_ref_data = test_admin.get_db(alt_ref)
        if ref_data == alt_ref_data:
            print("The databases are the same")
        else:
            print("The databases are not the same")
    def update_changed_db_iter(ref, url, iterate: str):
        changed=test_admin.get_changed_data(ref,url)
        count = 0
        for dict in changed:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def update_changed_db(ref, url):
        changed=test_admin.get_changed_data(ref,url)
        count = 0
        for dict in changed:
            ref.update({count: dict})
            count += 1
            print(count)
    def update_db(ref, alt_ref):
        alt_ref_data= test_admin.get_db(alt_ref)
        count = 0
        for dict in alt_ref_data:
            ref.update({count: dict})
            count += 1
            print(count)
    def update_db_iter(ref, alt_ref, iterate: str):
        alt_ref_data= test_admin.get_db(alt_ref)
        count = 0
        for dict in alt_ref_data:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def delete_node(ref):
        for node in ref.get():
            ref.child(node).delete()
    def add_to_db(ref, data):
        ref.push(data)

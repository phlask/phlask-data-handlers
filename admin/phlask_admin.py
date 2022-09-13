import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebaseadmin_module import get_db, get_changed_data, db_dry_count, db_comparison, update_changed_db_iter, update_changed_db, update_db, update_db_iter
from firebaseadmin_module import ListenerClass as ls
#----------------------------------------------------------------------------------------------------------------------
# Prod database URL's
pointer_url = "https://phlask-web-map-food-hours.firebaseio.com/"
prod_water_url_live = "https://phlask-web-map-prod-water-live.firebaseio.com/"
prod_water_url_verify = "https://phlask-web-map-prod-water-verify.firebaseio.com/"
prod_food_url_live = 'https://phlask-web-map-prod-food-live.firebaseio.com/'
prod_food_url_verify = 'https://phlask-web-map-food-hours.firebaseio.com/'
# Beta database URL's for all of the beta databases (These URL are dummys for now) please replace with actual URLs when ready
beta_water_url_live = "https://phlask-web-map-beta-water-live.firebaseio.com/"
beta_water_url_verify = "https://phlask-web-map-beta-water-verify.firebaseio.com/"
beta_water_url = 'https://phlask-web-map-beta.firebaseio.com/'
beta_forage_url = 'https://phlask-web-map-forage-beta.firebaseio.com/'
beta_bathrooms_url = 'https://phlask-web-map-bathrooms-beta.firebaseio.com/'
beta_food_url = 'https://phlask-web-map-food-hours-beta.firebaseio.com/'
#----------------------------------------------------------------------------------------------------------------------
cred = credentials.Certificate("phlask-web-map-firebase-adminsdk-i2ung-32bde7cd7a.json")
pointer_init =  firebase_admin.initialize_app(cred, { 'databaseURL': pointer_url}, name="pointer_app")
prod_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': prod_water_url_live }, name="prod_water_live") #name is the app name
prod_water_verify=firebase_admin.initialize_app(cred, { 'databaseURL': prod_water_url_verify }, name="prod_water_verify") #name is the app name
beta_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': beta_water_url_live }, name="beta_water_live") #name is the app name
beta_water_verify=firebase_admin.initialize_app(cred, { 'databaseURL': beta_water_url_verify }, name="beta_water_verify") #name is the app name
# prod_forage=firebase_admin.initialize_app(cred, { 'databaseURL': prod_forage_url },  name="prod_forage") 
# prod_bathrooms=firebase_admin.initialize_app(cred, { 'databaseURL': prod_bathrooms_url },  name="prod_bathrooms")
prod_food_live=firebase_admin.initialize_app(cred, { 'databaseURL': prod_food_url_live },  name="prod_food_live")
prod_food_verify=firebase_admin.initialize_app(cred, { 'databaseURL': prod_food_url_verify },  name="prod_food_verify")
#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the prod databases
pointer_db = db.reference("/", app= pointer_init)
prod_water_db_live = db.reference('/', app= prod_water_live)
prod_water_db_verify = db.reference('/', app= prod_water_verify)

# prod_forage_db = db.reference('/', app=prod_forage)
# prod_bathrooms_db = db.reference('/', app=prod_bathrooms)
prod_food_db_live = db.reference('/', app=prod_food_live)
prod_food_db_verify = db.reference('/', app=prod_food_verify)
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the beta databases (These Ref's are dummys for now) please replace with actual URLs when ready

beta_water_db_live = db.reference('/', app=beta_water_live)
beta_water_db_verify = db.reference('/', app=beta_water_verify)
# beta_forage_db = db.reference('/', app=prod_forage)
# beta_bathrooms_db = db.reference('/', app=prod_bathrooms)
# beta_food_db = db.reference('/', app=prod_food)
#----------------------------------------------------------------------------------------------------------------------
# Retrieves the nested data within the prod DBs 
# Returns in the form of dictionaries in a list

# print(get_db(prod_food_db_live))
# print(get_db(pointer_db))
update_db(prod_food_db_live, pointer_db)


#Create a admin class for prod, beta, and test
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import os

json_data = None

#----------------------------------------------------------------------------------------------------------------------
#creds for initializing firebase admin
try :
    with open('phlask.json') as f:
        json_data = json.load(f)

# if there is no json file, then this will use the environment variable

except FileNotFoundError:
    json_data = os.getenv('FIREBASE_CREDENTIALS')

cred = credentials.Certificate(json_data)

def get_firebase_url(dev_type, data_type, live_type):
    return f'https://phlask-web-map-{dev_type}-{data_type}-{live_type}.firebaseio.com/'


#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Prod DB's
prod_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("prod","water","live") }, name="prod_water_live") #name is the app name
prod_water_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("prod", "water", "verify") }, name="prod_water_verify") #name is the app name
prod_food_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("prod", "food", "live") }, name="prod_food_live") #name is the app name
prod_food_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("prod", "food", "verify") }, name="prod_food_verify") #name is the app name
prod_forage_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("prod", "foraging", "live") }, name="prod_forage_live") #name is the app name
prod_forage_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("prod", "foraging", "verify") }, name="prod_forage_verify") #name is the app name
prod_bathroom_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("prod", "bathroom", "live") }, name="prod_bathroom_live") #name is the app name
prod_bathroom_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("prod", "bathroom", "verify") }, name="prod_bathroom_verify") #name is the app name
#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Beta DB's
beta_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("beta", "water", "live" ) }, name="beta_water_live") #name is the app name
beta_water_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("beta", "water", "verify") }, name="beta_water_verify") #name is the app name
beta_food_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("beta", "food", "live") }, name="beta_food_live") #name is the app name
beta_food_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("beta", "food", "verify") }, name="beta_food_verify") #name is the app name
beta_forage_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("beta", "foraging", "live") }, name="beta_forage_live") #name is the app name
beta_forage_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("beta", "foraging", "verify") }, name="beta_forage_verify") #name is the app name
beta_bathroom_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("beta", "bathroom", "live") }, name="beta_bathroom_live") #name is the app name
beta_bathroom_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("beta", "bathroom", "verify") }, name="beta_bathroom_verify") #name is the app name
#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Test DB's
test_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("test", "water", "live") }, name="test_water_live") #name is the app name
test_water_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("test", "water", "verify") }, name="test_water_verify") #name is the app name
test_food_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("test", "food", "live") }, name="test_food_live") #name is the app name
test_food_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("test", "food", "verify") }, name="test_food_verify") #name is the app name
test_forage_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("test", "foraging", "live") }, name="test_forage_live") #name is the app name
test_forage_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("test", "foraging", "verify") }, name="test_forage_verify") #name is the app name
test_bathroom_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("test", "bathroom", "live") }, name="test_bathroom_live") #name is the app name
test_bathroom_verify=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("test", "bathroom", "verify") }, name="test_bathroom_verify") #name is the app name
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

class Admin:
    # Constructor that initializes the different databases for an Admin object
    def __init__(self, water_db_live, food_db_live, forage_db_live, bathroom_db_live):
        self.water_db_live = water_db_live
        self.food_db_live = food_db_live
        self.forage_db_live = forage_db_live
        self.bathroom_db_live = bathroom_db_live
    # Method to get data from a given database reference
    def getDb(self, ref):
        ref_db = ref.get()
        return ref_db

    # Method to set data in a given database reference
    def setDb(self, ref):
        ref_db = ref.set()
        return ref_db

    # Method to get changed data from a given database reference and URL
    def getChangedData(self, ref, url):
        changed = ref.get_if_changed(url)
        changed_dict_list = changed[1]
        return changed_dict_list

    # Method to count the number of changed data entries in a given database reference and URL
    def dbDryCount(self, ref, url):
        changed = self.getChangedData(ref, url)
        count = 0
        for dict in changed:
            if dict:
                count += 1
        print(count)

    # Method to compare two database references to see if their data is the same
    def dbComparison(self, ref, alt_ref):
        ref_data = self.getDb(ref)
        alt_ref_data = self.getDb(alt_ref)
        if ref_data == alt_ref_data:
            print("The databases are the same")
        else:
            print("The databases are not the same")

    # Method to update a given database reference with changed data from a URL, iterating through the data
    def updateChangedDbIter(self, ref, url, iterate: str):
        changed = self.getChangedData(ref, url)
        count = 0
        for dict in changed:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)

    # Method to update a given database reference with changed data from a URL
    def updateChangedDb(self, ref, url):
        changed = self.getChangedData(ref, url)
        count = 0
        for dict in changed:
            ref.update({count: dict})
            count += 1
            print(count)

    # Method to update a given database reference with data from another reference
    def updateDb(self, ref, alt_ref):
        alt_ref_data = self.getDb(alt_ref)
        count = 0
        for dict in alt_ref_data:
            ref.update({count: dict})
            count += 1
            print(count)

    # Method to update a given database reference with data from another reference, iterating through the data
    def updateDbIter(self, ref, alt_ref, iterate: str):
        alt_ref_data = self.getDb(alt_ref)
        count = 0
        for dict in alt_ref_data:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)

    # Method to delete a node from a given database reference
    def deleteNode(self, ref):
        for node in ref.get():
            ref.child(node).delete()

    # Method to add data to a given database reference
    def addToDb(self, ref, data):
        ref.push(data)

    # Method to count the number of entries in a given database reference
    def getCount(self, ref):
        count = 0
        for dict in self.getDb(ref):
            count += 1
        return count
    # Method to get a specific tap from a given database reference based on their unique tapnum
    def getTap(self, ref, tapnum):
        taps = self.getDb(ref)
        try:
            for tap in taps:
                try:
                    if tap['tapnum'] == tapnum:
                        return tap
                except:
                   pass
                try:
                    if tap['foodnum'] == tapnum:
                        return tap
                except:
                    pass
        except:
            pass

    # Method to delete a specific tap from a given database reference based on their tapnum number
    def deleteTap(self, ref, tapnum):
        try:
            ref.child(str(tapnum)).delete()
        except:
            print("No tap found")
            
    # Method to update a specific tap from a given database reference based on their tapnum number
    def updateTap(self, ref, tapnum, data):
        try:
            ref.child(str(tapnum)).update(data)
        except:
            print("No tap found")

class prodAdmin(Admin):
    def __init__(self):
        super().__init__(prod_water_db_live, prod_food_db_live, prod_forage_db_live, prod_bathroom_db_live)


class betaAdmin(Admin):
    def __init__(self):
        super().__init__(beta_water_db_live, beta_food_db_live, beta_forage_db_live, beta_bathroom_db_live)


class testAdmin(Admin):
    def __init__(self):
        super().__init__(test_water_db_live, test_food_db_live, test_forage_db_live, test_bathroom_db_live)

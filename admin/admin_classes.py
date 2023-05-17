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
def initialize_firebase_app(app_name, cred, database_url):
    try:
        return firebase_admin.get_app(app_name)
    except ValueError:
        return firebase_admin.initialize_app(cred, {'databaseURL': database_url}, name=app_name)


#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Prod DB's
prod_water_live = initialize_firebase_app("prod_water_live", cred, get_firebase_url("prod","water","live"))
prod_water_verify = initialize_firebase_app("prod_water_verify", cred, get_firebase_url("prod", "water", "verify"))
prod_food_live = initialize_firebase_app("prod_food_live", cred, get_firebase_url("prod", "food", "live"))
prod_food_verify = initialize_firebase_app("prod_food_verify", cred, get_firebase_url("prod", "food", "verify"))
prod_forage_live = initialize_firebase_app("prod_forage_live", cred, get_firebase_url("prod", "foraging", "live"))
prod_forage_verify = initialize_firebase_app("prod_forage_verify", cred, get_firebase_url("prod", "foraging", "verify"))
prod_bathroom_live = initialize_firebase_app("prod_bathroom_live", cred, get_firebase_url("prod", "bathroom", "live"))
prod_bathroom_verify = initialize_firebase_app("prod_bathroom_verify", cred, get_firebase_url("prod", "bathroom", "verify"))
#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Beta DB's
beta_water_live = initialize_firebase_app("beta_water_live", cred, get_firebase_url("beta", "water", "live"))
beta_water_verify = initialize_firebase_app("beta_water_verify", cred, get_firebase_url("beta", "water", "verify"))
beta_food_live = initialize_firebase_app("beta_food_live", cred, get_firebase_url("beta", "food", "live"))
beta_food_verify = initialize_firebase_app("beta_food_verify", cred, get_firebase_url("beta", "food", "verify"))
beta_forage_live = initialize_firebase_app("beta_forage_live", cred, get_firebase_url("beta", "foraging", "live"))
beta_forage_verify = initialize_firebase_app("beta_forage_verify", cred, get_firebase_url("beta", "foraging", "verify"))
beta_bathroom_live = initialize_firebase_app("beta_bathroom_live", cred, get_firebase_url("beta", "bathroom", "live"))
beta_bathroom_verify = initialize_firebase_app("beta_bathroom_verify", cred, get_firebase_url("beta", "bathroom", "verify"))
#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Test DB's
test_water_live = initialize_firebase_app("test_water_live", cred, get_firebase_url("test", "water", "live"))
test_water_verify = initialize_firebase_app("test_water_verify", cred, get_firebase_url("test", "water", "verify"))
test_food_live = initialize_firebase_app("test_food_live", cred, get_firebase_url("test", "food", "live"))
test_food_verify = initialize_firebase_app("test_food_verify", cred, get_firebase_url("test", "food", "verify"))
test_forage_live = initialize_firebase_app("test_forage_live", cred, get_firebase_url("test", "foraging", "live"))
test_forage_verify = initialize_firebase_app("test_forage_verify", cred, get_firebase_url("test", "foraging", "verify"))
test_bathroom_live = initialize_firebase_app("test_bathroom_live", cred, get_firebase_url("test", "bathroom", "live"))
test_bathroom_verify = initialize_firebase_app("test_bathroom_verify", cred, get_firebase_url("test", "bathroom", "verify"))
#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the live/verify prod databases

#Live
prod_water_db_live = db.reference('/', app= prod_water_live)
prod_food_db_live = db.reference('/', app= prod_food_live)
prod_forage_db_live = db.reference('/', app= prod_forage_live)
prod_bathroom_db_live = db.reference('/', app= prod_bathroom_live)

#Verify
prod_water_db_verify = db.reference('/', app= prod_water_verify)
prod_food_db_verify = db.reference('/', app= prod_food_verify)
prod_forage_db_verify = db.reference('/', app= prod_forage_verify)
prod_bathroom_db_verify = db.reference('/', app= prod_bathroom_verify)

#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the beta databases

#Live
beta_water_db_live = db.reference('/', app= beta_water_live)
beta_food_db_live = db.reference('/', app= beta_food_live)
beta_forage_db_live = db.reference('/', app= beta_forage_live)
beta_bathroom_db_live = db.reference('/', app= beta_bathroom_live)

#Verify
beta_water_db_verify = db.reference('/', app= beta_water_verify)
beta_food_db_verify = db.reference('/', app= beta_food_verify)
beta_forage_db_verify = db.reference('/', app= beta_forage_verify)
beta_bathroom_db_verify = db.reference('/', app= beta_bathroom_verify)

#----------------------------------------------------------------------------------------------------------------------
# Database References for all of the test databases

#Live
test_water_db_live = db.reference('/', app= test_water_live)
test_food_db_live = db.reference('/', app= test_food_live)
test_forage_db_live = db.reference('/', app= test_forage_live)
test_bathroom_db_live = db.reference('/', app= test_bathroom_live)

#Verify
test_water_db_verify = db.reference('/', app= test_water_verify)
test_food_db_verify = db.reference('/', app= test_food_verify)
test_forage_db_verify = db.reference('/', app= test_forage_verify)
test_bathroom_db_verify = db.reference('/', app= test_bathroom_verify)

#----------------------------------------------------------------------------------------------------------------------

class Admin:
    # Constructor that initializes the different databases for an Admin object
    def __init__(self, water_db_live, food_db_live, forage_db_live, bathroom_db_live, water_db_verify, food_db_verify, forage_db_verify, bathroom_db_verify):
        self.water_db_live = water_db_live
        self.food_db_live = food_db_live
        self.forage_db_live = forage_db_live
        self.bathroom_db_live = bathroom_db_live
        self.water_db_verify = water_db_verify
        self.food_db_verify = food_db_verify
        self.forage_db_verify = forage_db_verify
        self.bathroom_db_verify = bathroom_db_verify


    # Method to convert json fields to strings specifically for the hours field
    def convert_json_fields(self, record):
        for key in record:
            if isinstance(record[key], str) and key == 'hours':
                # print(f'Original: {record[key]}')
                try:
                    record[key] = json.loads(record[key].replace("'", '"'))
                    # print(f'Converted: {record[key]}')
                except json.JSONDecodeError as e:
                    print(f'Error converting field: {e}')
                    pass
        return record
    
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
            ref.child(str(int(tapnum))).update(data)
        except:
            print(data)
            print("No tap found")

        # Method to update a given database reference with data from another reference


    def updateDb(self, ref, dict_list):
        for record in dict_list:
            if isinstance(record, dict):
                tapnum = record.get('tapnum')
                if tapnum is not None:
                    record = self.convert_json_fields(record)
                    self.updateTap(ref, tapnum, record)
            else:
                print(f'Invalid record: {record}')



class prodAdmin(Admin):
    def __init__(self):
        super().__init__(prod_water_db_live, prod_food_db_live, prod_forage_db_live, prod_bathroom_db_live, prod_water_db_verify, prod_food_db_verify, prod_forage_db_verify, prod_bathroom_db_verify)


class betaAdmin(Admin):
    def __init__(self):
        super().__init__(beta_water_db_live, beta_food_db_live, beta_forage_db_live, beta_bathroom_db_live, beta_water_db_verify, beta_food_db_verify, beta_forage_db_verify, beta_bathroom_db_verify)


class testAdmin(Admin):
    def __init__(self):
        super().__init__(test_water_db_live, test_food_db_live, test_forage_db_live, test_bathroom_db_live, test_water_db_verify, test_food_db_verify, test_forage_db_verify, test_bathroom_db_verify)

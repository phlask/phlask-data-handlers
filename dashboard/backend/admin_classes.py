#Create a admin class for prod, beta, and test
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

json_data = None

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
try :
    import json
    with open('phlask.json') as f:
        json_data = json.load(f)

# if there is no json file, then this will use the environment variable

except FileNotFoundError:
    json_data = os.getenv('FIREBASE_CREDENTIALS')

cred = credentials.Certificate(json_data)
# firebase_admin.initialize_app(cred, { 'databaseURL': 'https://phlask-pyrebase-default-rtdb.firebaseio.com/' })

def get_firebase_url(dev_type, data_type, live_type):
    return f'https://phlask-web-map-{dev_type}-{data_type}-{live_type}.firebaseio.com/'


#----------------------------------------------------------------------------------------------------------------------
# initialize firebase admin Prod DB's
pointer_init =  firebase_admin.initialize_app(cred, { 'databaseURL': pointer_url}, name="pointer_app")
prod_water_live=firebase_admin.initialize_app(cred, { 'databaseURL': get_firebase_url("prod","water","live") }, name="prod_water_live") #name is the app name
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
class prodAdmin:
    def __init__(self):
        self.water_db_live = prod_water_db_live
        self.food_db_live = prod_food_db_live
        self.forage_db_live = prod_forage_db_live
        self.bathroom_db_live = prod_bathroom_db_live
    def getDb(ref):
        ref_db = ref.get()
        return ref_db
    def setDb(ref):
        ref_db = ref.set()
        return ref_db
    def getChangedData(ref,url):
        changed = ref.get_if_changed(url)
        changed_dict_list = changed[1]
        return changed_dict_list

    def dbDryCount(ref, url):
        changed=prodAdmin.getChangedData(ref,url)
        count = 0
        for dict in changed:
            if dict:
                count += 1
        print(count)
    def dbComparison(ref, alt_ref):
        ref_data = prodAdmin.getDb(ref)
        alt_ref_data = prodAdmin.getDb(alt_ref)
        if ref_data == alt_ref_data:
            print("The databases are the same")
        else:
            print("The databases are not the same")
    def updateChangedDbIter(ref, url, iterate: str):
        changed=prodAdmin.getChangedData(ref,url)
        count = 0
        for dict in changed:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def updateChangedDb(ref, url):
        changed=prodAdmin.getChangedData(ref,url)
        count = 0
        for dict in changed:
            ref.update({count: dict})
            count += 1
            print(count)
    def updateDb(ref, alt_ref):
        alt_ref_data= prodAdmin.getDb(alt_ref)
        count = 0
        for dict in alt_ref_data:
            ref.update({count: dict})
            count += 1
            print(count)
    def updateDbIter(ref, alt_ref, iterate: str):
        alt_ref_data= prodAdmin.getDb(alt_ref)
        count = 0
        for dict in alt_ref_data:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def deleteNode(ref):
        for node in ref.get():
            ref.child(node).delete()
    def addToDb(ref, data):
        ref.push(data)
    def getCount(ref):
        count = 0
        for dict in prodAdmin.getDb(ref):
            count += 1
        return count

    def getTap(ref, tapnum):
        taps = prodAdmin.getDb(ref)
        try:
            for tap in taps:
                try:
                    if tap['tapnum'] == tapnum:
                        return tap
                except:
                   pass
        except:
            pass
    def deleteTap(ref, tapnum):
        try:
            ref.child(str(tapnum)).delete()
                    
        except:
            print("No tap found")
    def updateTap(ref, tapnum, data):
        try:
            ref.child(str(tapnum)).update(data)
        except:
            print("No tap found")
            


class betaAdmin:
    def __init__(self):
        self.water_db_live = beta_water_db_live
        self.food_db_live = beta_food_db_live
        self.forage_db_live = beta_forage_db_live
        self.bathroom_db_live = beta_bathroom_db_live
    def getDb(ref):
        ref_db = ref.get()
        return ref_db
    def getChangedData(ref,url):
        changed = ref.get_if_changed(url)
        changed_dict_list = changed[1]
        return changed_dict_list

    def dbDryCount(ref, url):
        changed=betaAdmin.getChangedData(ref,url)
        count = 0
        for dict in changed:
            if dict:
                count += 1
        print(count)
    def dbComparison(ref, alt_ref):
        ref_data = betaAdmin.getDb(ref)
        alt_ref_data = betaAdmin.getDb(alt_ref)
        if ref_data == alt_ref_data:
            print("The databases are the same")
        else:
            print("The databases are not the same")
    def updateChangedDbIter(ref, url, iterate: str):
        changed=betaAdmin.getChangedData(ref,url)
        count = 0
        for dict in changed:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def updateChangedDb(ref, url):
        changed=betaAdmin.getChangedData(ref,url)
        count = 0
        for dict in changed:
            ref.update({count: dict})
            count += 1
            print(count)
    def updateDb(ref, alt_ref):
        alt_ref_data= betaAdmin.getDb(alt_ref)
        count = 0
        for dict in alt_ref_data:
            ref.update({count: dict})
            count += 1
            print(count)
    def updateDbIter(ref, alt_ref, iterate: str):
        alt_ref_data= betaAdmin.getDb(alt_ref)
        count = 0
        for dict in alt_ref_data:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def deleteNode(ref):
        for node in ref.get():
            ref.child(node).delete()
    def deleteTap(ref, tapnum):
        taps = betaAdmin.getDb(ref)
        for tap in taps:
            try:
                if tap['tapnum'] == tapnum:
                    ref.child(tap).delete()
            except:
                continue
    def addToDb(ref, data):
        ref.push(data)
    def getCount(ref):
        count = 0
        for dict in betaAdmin.getDb(ref):
            count += 1
        return count

    def getTap(ref, tapnum):
        taps = betaAdmin.getDb(ref)
        try:
            for tap in taps:
                try:
                    if tap['tapnum'] == tapnum:
                        return tap
                except:
                   pass
        except:
            pass
    def deleteTap(ref, tapnum):
        try:
            ref.child(str(tapnum)).delete()
                    
        except:
            print("No tap found")
    def updateTap(ref, tapnum, data):
        try:
            ref.child(str(tapnum)).update(data)
        except:
            print("No tap found")
            
    
    

class testAdmin:
    def __init__(self):
        self.water_db_live = test_water_db_live
        self.food_db_live = test_food_db_live
        self.forage_db_live = test_forage_db_live
        self.bathroom_db_live = test_bathroom_db_live
    def getDb(self, ref):
        ref_db = ref.get()
        return ref_db
    def getChangedData(ref,url):
        changed = ref.get_if_changed(url)
        changed_dict_list = changed[1]
        return changed_dict_list

    def dbDryCount(ref, url):
        changed=testAdmin.getChangedData(ref,url)
        count = 0
        for dict in changed:
            if dict:
                count += 1
        print(count)
    def dbComparison(ref, alt_ref):
        ref_data = testAdmin.getDb(ref)
        alt_ref_data = testAdmin.getDb(alt_ref)
        if ref_data == alt_ref_data:
            print("The databases are the same")
        else:
            print("The databases are not the same")
    def updateChangedDbIter(ref, url, iterate: str):
        changed=testAdmin.getChangedData(ref,url)
        count = 0
        for dict in changed:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def updateChangedDb(ref, url):
        changed=testAdmin.getChangedData(ref,url)
        count = 0
        for dict in changed:
            ref.update({count: dict})
            count += 1
            print(count)
    def updateDb(ref, alt_ref):
        alt_ref_data= testAdmin.getDb(alt_ref)
        count = 0
        for dict in alt_ref_data:
            ref.update({count: dict})
            count += 1
            print(count)
    def updateDbIter(ref, alt_ref, iterate: str):
        alt_ref_data= testAdmin.getDb(alt_ref)
        count = 0
        for dict in alt_ref_data:
            if dict[iterate] == count:
                ref.update({count: dict})
                count += 1
                print(count)
    def deleteNode(ref):
        for node in ref.get():
            ref.child(node).delete()
    def addToDb(ref, data):
        ref.push(data)

    def getCount(ref):
        count = 0
        for dict in testAdmin.getDb(ref):
            count += 1
        return count

    def getTap(ref, tapnum):
        taps = testAdmin.getDb(ref)
        try:
            for tap in taps:
                try:
                    if tap['tapnum'] == tapnum:
                        return tap
                except:
                   pass
        except:
            pass
    def deleteTap(ref, tapnum):
        try:
            ref.child(str(tapnum)).delete()
                    
        except:
            print("No tap found")
    def updateTap(ref, tapnum, data):
        try:
            ref.child(str(tapnum)).update(data)
        except:
            print("No tap found")
            
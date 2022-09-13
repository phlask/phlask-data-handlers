# Phlask Firebase Database re-model
#------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
from click import confirm
import pyrebase
import json
import os
import sys
# Config/Setup
#-------------------------------------------------------------------------------
# Firebase Config for Dummy Data
firebaseConfig = {
  "apiKey": "AIzaSyBwTdRWEOBNvMfMbvHOoi9TQeUjoX5AHuc",
  "authDomain": "phlask-pyrebase.firebaseapp.com",
  "databaseURL": "https://phlask-pyrebase-default-rtdb.firebaseio.com",
  "projectId": "phlask-pyrebase",
  "storageBucket": "phlask-pyrebase.appspot.com",
  "messagingSenderId": "987505470254",
  "appId": "1:987505470254:web:bc1a7c1dd74bba39fb68bf",
  "measurementId": "G-80XFK3L26M"
}
#-------------------------------------------------------------------------------
# Firebase Config for Real Data
# firebaseConfig = {
#   "apiKey": "AIzaSyA1dTfOeX5aXeHViJqiV-mT2iFUaasRcZc",
#   "authDomain": "phlask-web-map.firebaseapp.com",
#   "databaseURL": "https://phlask-web-map.firebaseio.com",
#   "projectId": "phlask-web-map",
#   "storageBucket": "phlask-web-map.appspot.com",
#   "messagingSenderId": "428394983826",
#   "appId": "1:428394983826:web:b81abdcfd5af5401e0514b",
#   "measurementId": "G-V5Q525QRK2"
# }
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
#-------------------------------------------------------------------------------
# Phlask Json import

# with open("2022-05-03T20_00_22Z_phlask-web-map_data.json", "r") as f:
#     d = json.load(f)
# print(d["0"])
# test correctley Located data in json file above


# with open("2022-05-03T20_00_22Z_phlask-web-map_data.json", "r") as f:
#     d = json.load(f)
# with open("phlask-web-map_data.json", "w") as f:
#     new_json=json.dump(d, f, indent=2)
# print(new_json)
# test correctley formats the json file above the same it is in the firebase


# with open("phlask-web-map_data.json", "r") as f:
#     d = json.load(f)
# print(d["0"])
# test correctly located data in restructured json file above

#-------------------------------------------------------------------------------
# User Authentication
# Signup
# email=input("Enter your email: ")
# password=input("Enter your password: ")
# confirm_password=input("Confirm your password: ")
# if password == confirm_password:
#     auth.create_user_with_email_and_password(email, password)


#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# User Authentication
# Login
# email=input("Enter your email: ")
# password=input("Enter your password: ")
# try:
#   auth.sign_in_with_email_and_password(email, password)
#   print("Login Successful")
# except:
#   print("Login Failed")


#-------------------------------------------------------------------------------
# Heiarachy of structure in future possibly
# data = {
#     'phlask-web-map':{
#         'phlask-web-map-test': {
#             'phlask-web-map-test-water': {
#                 'phlask-web-map-test-water-live': True,
#                 'phlask-web-map-test-water-verify': False,
#             },
#             'phlask-web-map-test-food': {
#                 'phlask-web-map-test-food-live': True,
#                 'phlask-web-map-test-food-verify': False,
#             },
#             'phlask-web-map-test-foraging': {
#                 'phlask-web-map-test-foraging-live': True,
#                 'phlask-web-map-test-foraging-verify': False,
#             },
#             'phlask-web-map-test-bathrooms': {
#                 'phlask-web-map-test-bathrooms-live': True,
#                 'phlask-web-map-test-bathrooms-verify': False,
#             },
#         },
#     },
# }
#-------------------------------------------------------------------------------
# Misc. Below
#'phlask-web-map-beta': 
#'phlask-web-map-prod':



#-------------------------------------------------------------------------------
# Create Data
# with open("phlask-web-map_data.json", "r") as f:
#     d = json.load(f)
# db.child("phlask-struct").push(d)
# db.child("phlask-struct").child("phlask-web-map").set(d)
#db.child("phlask-struct").push({"users": ""})
# dataread=db.child("phlask-struct").child("users").child("0").get()
# print(dataread.val())
#-------------------------------------------------------------------------------
# Read Data

dataread = db.child("phlask-web-map").get()
print(dataread)
#-------------------------------------------------------------------------------
# Update Data

#db.child("Phlask").child("phlask-web-map").update({"phlask-web-map-beta": {"phlask-web-map-beta-water": {"phlask-web-map-beta-water-live": True, "phlask-web-map-beta-water-verify": True}}})
#db.child("Phlask").child("phlask-web-map").update({"phlask-web-map-prod": {"phlask-web-map-prod-water": {"phlask-web-map-prod-water-live": True, "phlask-web-map-prod-water-verify": True}}})
# db.child("Phlask").child("phlask-web-map").child("phlask-web-map-prod").update({'phlask-web-map-prod-food': {
#     'phlask-web-map-prod-food-live': True,
#     'phlask-web-map-prod-food-verify': False,
# },
#     'phlask-web-map-prod-foraging': {
#     'phlask-web-map-prod-foraging-live': True,
#     'phlask-web-map-prod-foraging-verify': False,
# },
#     'phlask-web-map-prod-bathrooms': {
#     'phlask-web-map-prod-bathrooms-live': True,
#     'phlask-web-map-prod-bathrooms-verify': False,
# }
# })
#db.child("Hotel").child("Users").child("1").update({"email": "evandoe@gmail.com"})
#-------------------------------------------------------------------------------
# Remove Data

#Delete 1 Value (from all parent nodes)
#db.child("Hotel").child("Users").child("age").remove()

# Delete whole Node
#db.child("Hotel").child("Users").remove()

#-------------------------------------------------------------------------------
# Notes for tonight about Phlask Firebase Database
# The Main Data Structure is a dictionary of dictionaries for each node
# the Parent Nodes within the live data base are in the of string numbers. EX:"0"
# The live database is named "phlask-web-map"
# the Parent Nodes also act as the location for the data within the live database

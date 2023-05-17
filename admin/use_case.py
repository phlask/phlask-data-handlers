# Admin Classes Use Case Documentation/Tests

# 1. Import the required classes from the admin_classes module.
from admin_classes import prodAdmin, betaAdmin, testAdmin


#. 2 Initialize the prod, beta, and test environment database references.

# Initialize the prod_admin class
water_prod = prodAdmin().water_db_live
food_prod = prodAdmin().food_db_live
bathroom_prod = prodAdmin().bathroom_db_live
forage_prod = prodAdmin().forage_db_live

# Initialize the beta_admin class
water_beta = betaAdmin().water_db_live
food_beta = betaAdmin().food_db_live
bathroom_beta = betaAdmin().bathroom_db_live
forage_beta = betaAdmin().forage_db_live

# Initialize the test_admin class
water_test = testAdmin().water_db_live
food_test = testAdmin().food_db_live
bathroom_test = testAdmin().bathroom_db_live
forage_test = testAdmin().forage_db_live


# 3. Use the getDb() method to retrieve data from a specific database reference.
# data = prodAdmin().getDb(water_prod)
# print(data)


# 4. Use the getTap() method to retrieve data from a specific tap number.
# food = prodAdmin().getDb(food_prod)
tap = prodAdmin().getTap(food_prod, 2)
print(tap)

# To use this module outside of the admin directory without copying admin_classes.py, use the following code above the import statement:

# import sys
# import os
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# # Add the project root directory to the Python path
# sys.path.append(project_root)

# from admin.admin_classes import prodAdmin, betaAdmin, testAdmin

# Then proceed with the use case documentation/tests as normal:



#. 2 Initialize the prod, beta, and test environment database references.

# # Initialize the prod_admin class
# water_prod = prodAdmin().water_db_live
# food_prod = prodAdmin().food_db_live
# bathroom_prod = prodAdmin().bathroom_db_live
# forage_prod = prodAdmin().forage_db_live

# # Initialize the beta_admin class
# water_beta = betaAdmin().water_db_live
# food_beta = betaAdmin().food_db_live
# bathroom_beta = betaAdmin().bathroom_db_live
# forage_beta = betaAdmin().forage_db_live

# # Initialize the test_admin class
# water_test = testAdmin().water_db_live
# food_test = testAdmin().food_db_live
# bathroom_test = testAdmin().bathroom_db_live
# forage_test = testAdmin().forage_db_live


# # 3. Use the getDb() method to retrieve data from a specific database reference.
# data = prodAdmin().getDb(water_prod)
# print(data)


# Import all the modules
from admin_classes import prod_admin as prod
from admin_classes import beta_admin as beta
from admin_classes import test_admin as test

# initialize the prod_admin class
water_prod=prod()
food_prod=prod()
bathroom_prod=prod()
forage_prod=prod()
# initialize the beta_admin class
water_beta=beta()
food_beta=beta()
bathroom_beta=beta()
forage_beta=beta()
# initialize the test_admin class
water_test=test()
food_test=test()
bathroom_test=test()
forage_test=test()

# initialize the prod db reference
water_db_prod=water_prod.water_db_live
food_db_prod=food_prod.food_db_live
bathroom_db_prod=bathroom_prod.bathroom_db_live
forage_db_prod=forage_prod.forage_db_live

# initialize the beta db reference
water_db_beta=water_beta.water_db_live
food_db_beta=food_beta.food_db_live
bathroom_db_beta=bathroom_beta.bathroom_db_live
forage_db_beta=forage_beta.forage_db_live

# initialize the test db reference
water_db_test=water_test.water_db_live
food_db_test=food_test.food_db_live
bathroom_db_test=bathroom_test.bathroom_db_live
forage_db_test=forage_test.forage_db_live

#update beta db with prod db

def update_beta():
    prod.update_db(water_db_beta,water_db_prod)
    prod.update_db(food_db_beta,food_db_prod)
    prod.update_db(bathroom_db_beta,bathroom_db_prod)
    prod.update_db(forage_db_beta,forage_db_prod)

def update_test():
    prod.update_db(water_db_test,water_db_prod)
    prod.update_db(food_db_test,food_db_prod)
    prod.update_db(bathroom_db_test,bathroom_db_prod)
    prod.update_db(forage_db_test,forage_db_prod)

def full_update():
    update_beta()
    update_test()

def full_test():
    print(prod.get_db(water_db_prod))

    
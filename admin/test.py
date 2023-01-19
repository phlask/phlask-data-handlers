# Import all the modules
from admin_classes import prod_admin as prod
from admin_classes import pointer_init
# from admin_classes import beta_admin as beta
# from admin_classes import test_admin as test

# initialize the prod_admin class
water=prod()
food=prod()

# initialize the prod water db reference
water_db=water.water_db_live
food_db=food.food_db_live

#Example calls for the classes
# print(prod.get_db(water_db))
# print("----------------------------------------------")
# print("Checking if water_db and food_db contain the same data: "), prod.db_comparison(water_db,food_db), print("----------------------------------------------")

#    print("-----------------")

# print(prod.get_tap(water_db, 1))

# create a function to check how long it takes to run a function
def time_it(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return result
    return wrapper

#test the function
@time_it
def time_check():
    taps=[]
    # db_count = prod.get_count(water_db)
    for i in range(0, 274):
        taps_i = prod.get_tap(water_db, i)
        taps.append(taps_i)
    return taps[1]

# print(time_check())
# print("----------------------------------------------")



print(prod.get_tap(water_db, 1))


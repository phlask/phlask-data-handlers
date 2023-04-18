from flask import Flask, redirect, request
from flask_cors import CORS
import sys
from dotenv import load_dotenv
import json
import os

from admin_classes import prodAdmin as prod, betaAdmin as beta, testAdmin as test

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
# from admin.admin_classes import prodAdmin as prod, betaAdmin as beta, testAdmin as test

load_dotenv()
# initialize the prod_admin class
water_prod=prod().water_db_live
food_prod=prod().food_db_live
bathroom_prod=prod().bathroom_db_live
forage_prod=prod().forage_db_live
# initialize the beta_admin class
water_beta=beta().water_db_live
food_beta=beta().food_db_live
bathroom_beta=beta().bathroom_db_live
forage_beta=beta().forage_db_live
# initialize the test_admin class
water_test=test().water_db_live
food_test=test().food_db_live
bathroom_test=test().bathroom_db_live
forage_test=test().forage_db_live

dashboard = Flask(__name__)

CORS(dashboard)

def connectDB():
    return water_prod

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

@dashboard.route("/")
@time_it
def main():
    result = {}
    data = prod.getDb(water_prod)
    
    for tap in data:
        try:
            tapnum = tap["tapnum"]
            if tapnum not in result:
                result[tapnum] = {}
            result[tapnum]=tap
        except:
            pass
    return json.dumps(result)

@dashboard.route('/updatetap/<int:tapnum>', methods = ['GET', 'PUT'])
def updatetap(tapnum):
    tp=[]
    db=prod.getDb(water_prod) 
    if request.method == 'GET':
        try:
            tp = prod.getTap(water_prod, tapnum)
            return json.dumps(tp)
        except:
            pass

    elif request.method == 'PUT':
        try:
            data = request.get_json()
            water_prod.update({
                tapnum: {
                    "access": data.get("access"),
                    "address": data.get("address"),
                    "city": data.get("city"),
                    "description": data.get("description"),
                    "filteration": data.get("filtration"),
                    "gp_id": data.get("gp_id"),
                    "handicap": data.get("handicap"),
                    "latitude": data.get("lat"),
                    "longitude": data.get("lon"),
                    "norms": data.get("norms"),
                    "organization": data.get("organization"),
                    "permanently_closed": data.get("permanently_closed"),
                    "phone": data.get("phone"),
                    "quality": data.get("quality"),
                    "service": data.get("service"),
                    "statement": data.get("statement"),
                    "status": data.get("status"),
                    "tap_type": data.get("tap_type"),
                    "tapnum": data.get("tapnum"),
                    "vessel": data.get("vessel"),
                    "zip_code": data.get("zip_code")
                }
            })
            return f"Tap {tapnum} Updated Successfully"
        except:
            return f"Error updating tap {tapnum}"


@dashboard.route('/deletetap/<int:tapnum>')
def deletetap(tapnum):
    prod.deleteTap(water_prod, str(tapnum))
    return redirect('/') 

# Uncomment this to run the app locally without docker! Dont forget to do similar configuration for the frontend!

# if(__name__ == "__main__"): 
#     dbconn = connectDB()
#     dashboard.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)), debug=True)

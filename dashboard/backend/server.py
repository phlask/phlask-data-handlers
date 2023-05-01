from flask import Flask, redirect, request, render_template, jsonify
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
    data = prod().getDb(water_prod)
    
    for tap in data:
        try:
            tapnum = tap["tapnum"]
            if tapnum not in result:
                result[tapnum] = {}
            result[tapnum]=tap
        except:
            pass
    return json.dumps(result)


# @dashboard.route('/chart-data')
# def chart_data():
#     data = {
#         'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
#         'datasets': [
#             {
#                 'label': 'My First Dataset',
#                 'data': [65, 59, 80, 81, 56, 55, 40],
#                 'fill': False,
#                 'borderColor': 'rgb(75, 192, 192)'
#             }
#         ]
#     }
#     return jsonify(data)



# Initiating the count of taps in each database
water_prod_count = prod().getCount(water_prod)
food_prod_count = prod().getCount(food_prod)
bathroom_prod_count = prod().getCount(bathroom_prod)
forage_prod_count = prod().getCount(forage_prod)

# Create a route to send the formated chart data to the frontend
@dashboard.route('/chart-data')
def chart_data():
    data = {
        'labels': ['Water DB', 'Food DB', 'Bathroom DB', 'Forage DB'],
        'datasets': [
            {
                'label': 'Water Tap Count',
                'data': [water_prod_count, 0, 0, 0],
                'backgroundColor': 'rgba(75, 192, 192, 0.5)',
                'borderColor': 'rgb(75, 192, 192)',
                'borderWidth': 1,
                'hoverBackgroundColor': 'rgb(75, 192, 192)',
                'hoverBorderColor': 'rgba(75, 192, 192, 0.8)',
                'hoverBorderWidth': 2,
            },
            {
                'label': 'Food Tap Count',
                'data': [0, food_prod_count, 0, 0],
                'backgroundColor': 'rgba(255, 99, 132, 0.5)',
                'borderColor': 'rgb(255, 99, 132)',
                'borderWidth': 1,
                'hoverBackgroundColor': 'rgb(255, 99, 132)',
                'hoverBorderColor': 'rgba(255, 99, 132, 0.8)',
                'hoverBorderWidth': 2,
            },
            {
                'label': 'Bathroom Tap Count',
                'data': [0, 0, bathroom_prod_count, 0],
                'backgroundColor': 'rgba(54, 162, 235, 0.5)',
                'borderColor': 'rgb(54, 162, 235)',
                'borderWidth': 1,
                'hoverBackgroundColor': 'rgb(54, 162, 235)',
                'hoverBorderColor': 'rgba(54, 162, 235, 0.8)',
                'hoverBorderWidth': 2,
            },
            {
                'label': 'Forage Tap Count',
                'data': [0, 0, 0, forage_prod_count],
                'backgroundColor': 'rgba(255, 205, 86, 0.5)',
                'borderColor': 'rgb(255, 205, 86)',
                'borderWidth': 1,
                'hoverBackgroundColor': 'rgb(255, 205, 86)',
                'hoverBorderColor': 'rgba(255, 205, 86, 0.8)',
                'hoverBorderWidth': 2,
            }
        ]
    }
    return jsonify(data)



@dashboard.route('/updatetap/<int:tapnum>', methods = ['GET', 'PUT'])
def updatetap(tapnum):
    tp=[]
    db=prod().getDb(water_prod) 
    if request.method == 'GET':
        try:
            tp = prod().getTap(water_prod, tapnum)
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

if(__name__ == "__main__"): 
    dbconn = connectDB()
    dashboard.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)), debug=True)

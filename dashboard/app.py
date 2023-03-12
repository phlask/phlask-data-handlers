from flask import Flask, render_template, redirect, url_for, send_from_directory, request, jsonify, current_app, g as app_ctx
from admin_classes import prodAdmin as prod, betaAdmin as beta, testAdmin as test
import os
import time
import random as rand


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
    
    for d in data:
        try:
            tapnum = d["tapnum"]
            # print(tapnum)
            if tapnum not in result:
                result[tapnum] = {}
            result[tapnum]=d
        except:
            pass

    return render_template("index.html", taps=result)

@dashboard.route("/addtap", methods = ['GET','POST'])
def addtapp():
    tapcount = prod.getCount(water_prod)
    if request.method == 'GET':
        return render_template("addtap.html", tap = {})
    if request.method == 'POST':
        try:
            access = str(request.form["access"])
            address = str(request.form["address"])
            city = str(request.form["city"])
            description = str(request.form["description"])
            filteration = str(request.form["filtration"])
            gp_id = str(request.form["gp_id"])
            handicap = str(request.form["handicap"])
            hours = str(request.form["hours"])
            latitude = float(request.form["lat"])
            longitude = float(request.form["lon"])
            norms = str(request.form["norms"])
            organization = str(request.form["organization"])
            permanently_closed = str(request.form["permanently_closed"])
            phone = str(request.form["phone"])
            quality = str(request.form["quality"])
            service= str(request.form["service"])
            statement = str(request.form["statement"])
            status = str(request.form["status"])
            tap_type = str(request.form["tap_type"])
            tapnum = int(request.form["tapnum"])
            vessel = str(request.form["vessel"])
            zip_code = str(request.form["zip_code"])
            water_prod.update({tapcount: 
            { "access": access, "address": address, "city": city, "description": description, "filteration": filteration, "gp_id":gp_id,"handicap":handicap , "latitude": latitude, "longitude": longitude, "norms": norms, "organization": organization, "permanently_closed": permanently_closed, "phone": phone, "quality": quality, "service": service, "statement": statement, "status": status, "tap_type": tap_type, "tapnum": tapnum, "vessel": vessel, "zip_code": zip_code } } )
            return redirect('/')
        except:
            access = str(request.form["access"])
            address = str(request.form["address"])
            city = str(request.form["city"])
            description = str(request.form["description"])
            filteration = str(request.form["filtration"])
            gp_id = str(request.form["gp_id"])
            handicap = str(request.form["handicap"])
            hours = str(request.form["hours"])
            latitude = int(request.form["lat"])
            longitude = int(request.form["lon"])
            norms = str(request.form["norms"])
            organization = str(request.form["organization"])
            permanently_closed = str(request.form["permanently_closed"])
            phone = str(request.form["phone"])
            quality = str(request.form["quality"])
            service= str(request.form["service"])
            statement = str(request.form["statement"])
            status = str(request.form["status"])
            tap_type = str(request.form["tap_type"])
            tapnum = int(request.form["tapnum"])
            vessel = str(request.form["vessel"])
            zip_code = str(request.form["zip_code"])
            water_prod.update({tapcount: 
            { "access": access, "address": address, "city": city, "description": description, "filteration": filteration, "gp_id":gp_id,"handicap":handicap, "hours":hours , "latitude": latitude, "longitude": longitude, "norms": norms, "organization": organization, "permanently_closed": permanently_closed, "phone": phone, "quality": quality, "service": service, "statement": statement, "status": status, "tap_type": tap_type, "tapnum": tapnum, "vessel": vessel, "zip_code": zip_code } } )
            return redirect('/')

@dashboard.route('/updatetap/<int:tapnum>', methods = ['GET','POST'])
def updatetap(tapnum):
    tp=[]
    db=prod.getDb(water_prod) 
    if request.method == 'GET':
        try:
            tp = prod.getTap(water_prod, tapnum)
            return render_template("addtap.html", tap = tp)
        except:
            pass
      
    if request.method == 'POST':
        try:
            access = str(request.form["access"])
            address = str(request.form["address"])
            city = str(request.form["city"])
            description = str(request.form["description"])
            filteration = str(request.form["filtration"])
            gp_id = str(request.form["gp_id"])
            handicap = str(request.form["handicap"])
            # hours = str(request.form["hours"])
            latitude = int(request.form["lat"])
            longitude = int(request.form["lon"])
            norms = str(request.form["norms"])
            organization = str(request.form["organization"])
            permanently_closed = str(request.form["permanently_closed"])
            phone = str(request.form["phone"])
            quality = str(request.form["quality"])
            service= str(request.form["service"])
            statement = str(request.form["statement"])
            status = str(request.form["status"])
            tap_type = str(request.form["tap_type"])
            tapnum = int(request.form["tapnum"])
            vessel = str(request.form["vessel"])
            zip_code = str(request.form["zip_code"])
            water_prod.update({tapnum: { "access": access, "address": address, "city": city, "description": description, "filteration": filteration, "gp_id":gp_id,"handicap":handicap , "latitude": latitude, "longitude": longitude, "norms": norms, "organization": organization, "permanently_closed": permanently_closed, "phone": phone, "quality": quality, "service": service, "statement": statement, "status": status, "tap_type": tap_type, "tapnum": tapnum, "vessel": vessel, "zip_code": zip_code } } )
            return redirect('/')
        except:
            access = str(request.form["access"])
            address = str(request.form["address"])
            city = str(request.form["city"])
            description = str(request.form["description"])
            filteration = str(request.form["filtration"])
            gp_id = str(request.form["gp_id"])
            handicap = str(request.form["handicap"])
            # hours = str(request.form["hours"])
            latitude = float(request.form["lat"])
            longitude = float(request.form["lon"])
            norms = str(request.form["norms"])
            organization = str(request.form["organization"])
            permanently_closed = str(request.form["permanently_closed"])
            phone = str(request.form["phone"])
            quality = str(request.form["quality"])
            service= str(request.form["service"])
            statement = str(request.form["statement"])
            status = str(request.form["status"])
            tap_type = str(request.form["tap_type"])
            tapnum = int(request.form["tapnum"])
            vessel = str(request.form["vessel"])
            zip_code = str(request.form["zip_code"])
            water_prod.update({tapnum: 
            { "access": access, "address": address, "city": city, "description": description, "filteration": filteration, "gp_id":gp_id,"handicap":handicap , "latitude": latitude, "longitude": longitude, "norms": norms, "organization": organization, "permanently_closed": permanently_closed, "phone": phone, "quality": quality, "service": service, "statement": statement, "status": status, "tap_type": tap_type, "tapnum": tapnum, "vessel": vessel, "zip_code": zip_code } } )
            return redirect('/')

@dashboard.route('/deletetap/<int:tapnum>')
def deletetap(tapnum):
    prod.deleteTap(water_prod, str(tapnum))
    return redirect('/') 

@dashboard.route('/viewtap/<int:tapnum>', methods = ['GET','POST'])
def viewtap(tapnum):
    if request.method == 'GET':
        try:
            tp = prod.getTap(water_prod, tapnum)
            return render_template("viewtap.html", tap = tp)
        except:
            pass
    if request.method == 'POST':
        try:
            access = str(request.form["access"])
            address = str(request.form["address"])
            city = str(request.form["city"])
            description = str(request.form["description"])
            filteration = str(request.form["filtration"])
            gp_id = str(request.form["gp_id"])
            handicap = str(request.form["handicap"])
            hours = str(request.form["hours"])
            latitude = int(request.form["lat"])
            longitude = int(request.form["lon"])
            norms = str(request.form["norms"])
            organization = str(request.form["organization"])
            permanently_closed = str(request.form["permanently_closed"])
            phone = str(request.form["phone"])
            quality = str(request.form["quality"])
            service= str(request.form["service"])
            statement = str(request.form["statement"])
            status = str(request.form["status"])
            tap_type = str(request.form["tap_type"])
            tapnum = int(request.form["tapnum"])
            vessel = str(request.form["vessel"])
            zip_code = str(request.form["zip_code"])
            water_prod.update({tapnum: { "access": access, "address": address, "city": city, "description": description, "filteration": filteration, "gp_id":gp_id,"handicap":handicap , "latitude": latitude, "longitude": longitude, "norms": norms, "organization": organization, "permanently_closed": permanently_closed, "phone": phone, "quality": quality, "service": service, "statement": statement, "status": status, "tap_type": tap_type, "tapnum": tapnum, "vessel": vessel, "zip_code": zip_code } } )
            return redirect('/')
        except:
            access = str(request.form["access"])
            address = str(request.form["address"])
            city = str(request.form["city"])
            description = str(request.form["description"])
            filteration = str(request.form["filtration"])
            gp_id = str(request.form["gp_id"])
            handicap = str(request.form["handicap"])
            hours = str(request.form["hours"])
            latitude = float(request.form["lat"])
            longitude = float(request.form["lon"])
            norms = str(request.form["norms"])
            organization = str(request.form["organization"])
            permanently_closed = str(request.form["permanently_closed"])
            phone = str(request.form["phone"])
            quality = str(request.form["quality"])
            service= str(request.form["service"])
            statement = str(request.form["statement"])
            status = str(request.form["status"])
            tap_type = str(request.form["tap_type"])
            tapnum = int(request.form["tapnum"])
            vessel = str(request.form["vessel"])
            zip_code = str(request.form["zip_code"])
            water_prod.update({tapnum: 
            { "access": access, "address": address, "city": city, "description": description, "filteration": filteration, "gp_id":gp_id,"handicap":handicap ,"hours":hours , "latitude": latitude, "longitude": longitude, "norms": norms, "organization": organization, "permanently_closed": permanently_closed, "phone": phone, "quality": quality, "service": service, "statement": statement, "status": status, "tap_type": tap_type, "tapnum": tapnum, "vessel": vessel, "zip_code": zip_code } } )
            return redirect('/')
                
# @app.route('/favicon.ico') 
# def favicon(): 
#     return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='images/vnd.microsoft.icon')


# @dashboard.before_request
# def logging_before():
#     # Store the start time for the request
#     app_ctx.start_time = time.perf_counter()


# @dashboard.after_request
# def logging_after(response):
#     # Get total time in milliseconds
#     total_time = time.perf_counter() - app_ctx.start_time
#     time_in_ms = int(total_time * 1000)
#     # Log the time taken for the endpoint 
#     current_app.logger.info('%s ms %s %s %s', time_in_ms, request.method, request.path, dict(request.args))
#     return response


if(__name__ == "__main__"): 
    dbconn = connectDB()
    dashboard.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)),use_reloader=True, debug=True, TEMPLATES_AUTO_RELOAD=True)

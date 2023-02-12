from flask import Flask, render_template, redirect, url_for, send_from_directory, request, jsonify, current_app, g as app_ctx
from admin_classes import prod_admin as prod, beta_admin as beta, test_admin as test, json_data
import time
import os
import json
import boto3

os.environ['AWS_ACCESS_KEY_ID'] = 'PLACE_AWS_ID_HERE'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'PLACE_AWS_KEY_HERE'
s3 = boto3.client('s3')

bucket = 'phlask-firebase-bucket'
object_key = 'phlask.json'
response = s3.get_object(Bucket=bucket, Key=object_key)
object_content = response['Body'].read().decode('utf-8')
json_data = json.loads(object_content)


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

@dashboard.route("/")
def main():
    try:
        #Static 4 taps for testing
        # water_prod_1=prod.get_tap(water_prod, 1)
        # water_prod_2=prod.get_tap(water_prod, 2)
        # water_prod_3=prod.get_tap(water_prod, 3)
        # water_prod_4=prod.get_tap(water_prod, 4)
        # taps = [water_prod_1, water_prod_2, water_prod_3, water_prod_4]
#------------------------------------------------------------------------------------------------#
         # All taps for development
        taps=[]
        db_count = prod.get_count(water_prod)
        for i in range(0, db_count):
            taps_i = prod.get_tap(water_prod, i)
            taps.append(taps_i)

        return render_template("index.html", taps=taps)
    except:
        #if tapnum is not found in database on  /test
        pass
    # return render_template("test.html")

@dashboard.route("/addtap", methods = ['GET','POST'])
def addtapp():
    tapcount = prod.get_count(water_prod)
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
    db=prod.get_db(water_prod) 
    if request.method == 'GET':
        try:
            tp = prod.get_tap(water_prod, tapnum)
            return render_template("addtap.html", tap = tp)
        except:
            pass
        # for tap in db:
        #     if tap["tapnum"] == tapnum:
        #         prod.get_tap(water_prod,tapnum)
        #         tp.append(tap)
        # return render_template("addtap.html", tap = tp)
        
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
    prod.delete_tap(water_prod, str(tapnum))
    return redirect('/') 

@dashboard.route('/viewtap/<int:tapnum>', methods = ['GET','POST'])
def viewtap(tapnum):
    if request.method == 'GET':
        try:
            tp = prod.get_tap(water_prod, tapnum)
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

#original code for viewtap route
# @dashboard.route("/oldpage")
# def oldpage():
    # try:
        #Static 4 taps for testing
        # water_prod_1=prod.get_tap(water_prod, 1)
        # water_prod_2=prod.get_tap(water_prod, 2)
        # water_prod_3=prod.get_tap(water_prod, 3)
        # water_prod_4=prod.get_tap(water_prod, 4)
        # taps = [water_prod_1, water_prod_2, water_prod_3, water_prod_4]

        # All taps for development
        # taps=[]
        # db_count = prod.get_count(water_prod)
        # for i in range(0, db_count):
        #     taps_i = prod.get_tap(water_prod, i)
        #     taps.append(taps_i)
    #     return render_template("index.html", taps=taps)
    # except:
    #     pass

@dashboard.before_request
def logging_before():
    # Store the start time for the request
    app_ctx.start_time = time.perf_counter()


@dashboard.after_request
def logging_after(response):
    # Get total time in milliseconds
    total_time = time.perf_counter() - app_ctx.start_time
    time_in_ms = int(total_time * 1000)
    # Log the time taken for the endpoint 
    current_app.logger.info('%s ms %s %s %s', time_in_ms, request.method, request.path, dict(request.args))
    return response
# once database is loaded cache it

if(__name__ == "__main__"):
    dbconn = connectDB()
    dashboard.run(debug=True)

# Phlask Data Handlers
## This project is a toolset of Admin like data tools/scripts for the Phlask project

## Project Structure

```
.
├── admin
│   ├── admin_classes.py          <-- Custom Firebase's SDK Module Phlask use cases
│   ├── test.py                   <-- Testing script for new functions added to module
│   └── requirements.txt          <-- Required dependencies for usage 
├── aws_lambda                    <-- Componenets used in AWS for lambda functions
├── dashboard
|   ├──templates                  <-- Flask template HTML files located here
|   ├──docker-compose.yml
|   ├──Dockerfile                 <-- Dockerfile defining container for local dev and deploy
│   ├── admin_classes.py          <-- Custom Firebase's SDK Module Phlask use cases
│   ├── app.py                    <-- Main Flask app located here
│   ├── static                    <-- Static Assets for Webapp located here
│   └── integration               <-- Source files for unit tests
├── slackbot
|   ├── bot.py                    <-- Slackbot database update script located here 
│   └── requirements.txt          <-- Required dependencies for usage 
├── cypress.json
├── .env                          <-- Input Credentials/Paths for Slackbot & Firebase(not for dashboard usage)
├── README.md
└── cleanup.py                    <-- Script to clean up credentials and paths (call this before pushing commits)

```

### Features
- Flask Firebase CRUD Dashboard: Allows developers to easily view, update, delete, and sort/filter for taps

- Phlask Firebase Module: Contains a set of python functions to make complex queries simpler with Firebases RTDB 

- AWS Lambda Function Code Snippet: The code snippet is utilized for the AWS lambda function to make daily updates to the Beta & Test databases

- Firebase Slackbot: *Still in early development


### How to run dashboard web app
1. Start up terminal and CD in to the dashboard directory
2. Run the following commands while docker is running

```terminal
$ docker build -t dashboard .
```
Then run
```terminal
$ docker compose up
```
3. Then go to your browser and go to "http://127.0.0.1:5000/" to view and use the dashboard
**Warning Initial Run time is about ~50 seconds using the "all tap" develeopment mode. For now, to develop faster on the UI, plesase use the "static" mode for faster reload times. 
**Auto-reload is also wonky ccurrentley with how docker is set up. Edits done in app.py will make the application reload but not edits made in the templates folder. So keep in mind, you must alter something (Simply a space or delete a space) in the app.py file to see frontend changes. We will be working on improving this very soon! 

Example For faster development:

Uncomment the top block and comment out the bottom in app.py (excluding the return statemens and the code below)
#### app.py　

```python
@dashboard.route("/")
def main():
    try:
#Static 4 taps for testing
        # water_prod_1=prod.get_tap(water_prod, 1)
        # water_prod_2=prod.get_tap(water_prod, 2)
        # water_prod_3=prod.get_tap(water_prod, 3)
        # water_prod_4=prod.get_tap(water_prod, 4)
        # taps = [water_prod_1, water_prod_2, water_prod_3, water_prod_4]
#------------------------------------------------------------------------------#
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
```
*As this project is still in devlopment there are still loading speed issues that are still being taken care of
### Home Screen
![](https://github.com/ojimba01/phlask-admin/blob/main/readme/dashboard_index.gif)

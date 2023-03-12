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
│   └── requirements.txt          <-- Required dependencies for usage 
├── slack
|   ├── bot.py                    <-- Slackbot database update script located here 
│   └── requirements.txt          <-- Required dependencies for usage 
├── .env                          <-- Input Credentials/Paths for Slackbot & Firebase(not for dashboard usage)
├── README.md
└── cleanup.py                    <-- Script to clean up credentials and paths (call this before pushing commits)

```

### Features
- Flask Firebase CRUD Dashboard: Allows developers to easily view, update, delete, and sort/filter for taps

- Phlask Firebase Module: Contains a set of python functions to make complex queries simpler with Firebases RTDB 

- AWS Lambda Function Code Snippet: The code snippet is utilized for the AWS lambda function to make daily updates to the Beta & Test databases

- Firebase Slackbot: *Still in early development

## How to Run Dashboard Locally

### Docker (Recommended path for consistency across computers)

1. Start up terminal and CD in to the dashboard directory
2. Run the following commands while docker is running (do not include "$" while running the commands below)

```terminal
$ docker build -t dashboard .
```
3. Then run
```terminal
$ docker compose up
```
4. Then go to your browser and go to "http://127.0.0.1:5000/" to view and use the dashboard

<br/>

**Warning Initial Run time is about ~50 seconds using the "all tap" develeopment mode. For now, to develop faster on the UI, plesase use the "static" mode for faster reload times.

<br/>

**Auto-reload is also wonky ccurrentley with how docker is set up. Edits done in app.py will make the application reload but not edits made in the templates folder. So keep in mind, you must alter something (Simply a space or delete a space) in the app.py file to see frontend changes. We will be working on improving this very soon!
<br/>
### Flask (alternative)
1. Start up terminal and CD in to the dashboard directory
2. Run pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)
3. Then run the following script

```terminal
$ flask run
```
4. Then go to your browser and go to "http://127.0.0.1:5000/" to view and use the dashboard

### Home Screen
![](https://github.com/ojimba01/phlask-admin/blob/main/readme/dashboard_index.gif)

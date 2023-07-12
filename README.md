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
├── dashboard_st
|   ├──backend
|   ├── server.py              <-- Main Flask app located here
|   ├── admin_classes.py
|   ├── .env
│   └── requirements.txt       <-- Required dependencies for usage 
|   ├──frontend
|      ├── src
|           ├── App.tsx
|           ├── Components        <-- Source for all TypeScript React components
│           └── Assets            
|      └── index.html
|   ├──docker-compose.yml
|   ├──Dockerfile                 <-- Dockerfile defining container for local dev and deploy
│   ├── admin_classes.py          <-- Custom Firebase's SDK Module Phlask use cases
│   ├── static                    <-- Static Assets for Webapp located here
│   └── requirements.txt          <-- Required dependencies for usage 
├── README.md
└── cleanup.py                    <-- Script to clean up credentials and paths (call this before pushing commits)

```

### Features
- Flask Firebase CRUD Dashboard: Allows developers to easily view, update, delete, and sort/filter for taps

- Phlask Firebase Module: Contains a set of python functions to make complex queries simpler with Firebases RTDB 

- AWS Lambda Function Code Snippet: The code snippet is utilized for the AWS lambda function to make daily updates to the Beta & Test databases

## How to Run Dashboard Locally

### Docker (Recommended path for consistency across computers)

1. Start up terminal and CD in to the dashboard directory
2. Run the following commands while docker is running (do not include "$" while running the commands below)

```terminal
$ docker-compose up --build 
```
3. Then go to your browser and go to "http://localhost:5137/" to view and use the dashboard

*** When you are done with development use ctrl + c

*** Once the container and images are built you can just use "docker-compose up to" boot up the webapp without the build tag

```terminal
$ docker-compose up
```

<br/>

### Flask (alternative)

1. Start up terminal and CD in to the dashboard/backend directory 
2. Run pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)
3. Then run the following: "python server.py" in the dashboard/backend directory 

*** Make sure this line in server.py is uncommeted before step 3

```python
if(__name__ == "__main__"): 
    dbconn = connectDB()
    dashboard.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)), debug=True)

```
4. Then go to your browser and go to "http://127.0.0.1:5000/" to make sure the API is working fine

5. Then open a new terminal and CD into dashboard/backend

6. Make sure you are using Node 19 and run "npm install"

7. Once packages have updated run "npm run dev"
8. Then go to your browser and go to "http://localhost:5137/" to view and use the dashboard


### Home Screen
![](https://github.com/ojimba01/phlask-admin/blob/main/readme/dashboard_index.gif)
***This home screen is deprecated and will be updated soon

import os

def clean_aws_creds():
    changes_made = 0
    for root, dirs, files in os.walk("."):
        for file_name in files:
            if file_name.endswith(".py") and file_name != "cleanup.py":
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                with open(file_path, 'w') as file:
                    for line in lines:
                        if "os.environ['AWS_ACCESS_KEY_ID']" in line and not "os.environ['AWS_ACCESS_KEY_ID'] = 'PLACE_AWS_ID_HERE'" in line:
                            line = "os.environ['AWS_ACCESS_KEY_ID'] = 'PLACE_AWS_ID_HERE'\n"
                            changes_made += 1
                        elif "os.environ['AWS_SECRET_ACCESS_KEY']" in line and not "os.environ['AWS_SECRET_ACCESS_KEY'] = 'PLACE_AWS_KEY_HERE'" in line:
                            line = "os.environ['AWS_SECRET_ACCESS_KEY'] = 'PLACE_AWS_KEY_HERE'\n"
                            changes_made += 1
                        file.write(line)
    if changes_made == 0:
        print("AWS cleanup complete, no changes made.")
    elif changes_made == 1:
        print("AWS cleanup complete, 1 change made.")
    else:
        print("AWS cleanup complete, {} changes made.".format(changes_made))
def clean_slack_creds():
    changes_made = 0
    for root, dirs, files in os.walk("."):
        for file_name in files:
            if file_name.endswith(".env") and file_name != "cleanup.py":
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                with open(file_path, 'w') as file:
                    for line in lines:
                        if "SLACK_BOT_TOKEN=" in line and not "SLACK_BOT_TOKEN=ENTER_TOKEN_HERE" in line:
                            line = "SLACK_BOT_TOKEN=ENTER_TOKEN_HERE\n"
                            changes_made += 1
                        file.write(line)
    if changes_made == 0:
        print("Slack cleanup complete, no changes made.")
    elif changes_made == 1:
        print("Slack cleanup complete, 1 change made.")
    else:
        print("Slack cleanup complete, {} changes made.".format(changes_made))
def clean_firebase_path():
    changes_made = 0
    for root, dirs, files in os.walk("."):
        for file_name in files:
            if file_name.endswith(".env") and file_name != "cleanup.py":
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                with open(file_path, 'w') as file:
                    for line in lines:
                        if "FIREBASE_CREDENTIALS=" in line and not "FIREBASE_CREDENTIALS=/path/to/credentials.json" in line:
                            line = "FIREBASE_CREDENTIALS=/path/to/credentials.json\n"
                            changes_made += 1
                        file.write(line)
    if changes_made == 0:
        print("Firebase cleanup complete, no changes made.")
    elif changes_made == 1:
        print("Firebase cleanup complete, 1 change made.")
    else:
        print("Firebase cleanup complete, {} changes made.".format(changes_made))

if __name__ == '__main__':
    clean_aws_creds()
    clean_slack_creds()
    clean_firebase_path()

from update_script import fullTest, fullUpdate
import json
def lambdaHandler(event, context):
    
    fullTest()
    # full_update()
    return {
        'statusCode': 200,
        'body': json.dumps('Access to Phlask Firebase RTDB is confirmed!')
    }

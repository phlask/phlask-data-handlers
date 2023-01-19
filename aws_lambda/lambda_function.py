from update_script import full_test, full_update
import json
def lambda_handler(event, context):
    
    full_test()
    # full_update()
    return {
        'statusCode': 200,
        'body': json.dumps('Access to Phlask Firebase RTDB is confirmed!')
    }

import json
import json

def lambda_handler(event, context):
    # TODO implement
   # print(event)
    n1 = event['name']
    n2 = event['type']
    #print(n1)
    #print(context)
    return {
        'statusCode': 200,
        'firstname':  n1,
        'type': n2
    }

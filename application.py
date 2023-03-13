import json
import json
import boto3
def lambda_handler(event, context):
    # TODO implement
   # print(event)
    n1 = event['name']
    n2 = event['type']
    #n3 = event['caseid']
    #n4 = event['age']
    #print(n1)
    #print(context)
    if n2 == 'lname':
        state = 'lname'
    else:
        state = 'fname'
    sf = boto3.client('stepfunctions', region_name = 'eu-west-2')
    input_dict = {'state': state, 'name': n1}
    response = sf.start_execution(
    stateMachineArn = 'arn:aws:states:eu-west-2:918781784251:stateMachine:sourabhfsm',
    input = json.dumps(input_dict))
    return input_dict
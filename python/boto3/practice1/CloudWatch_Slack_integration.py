'''
CloudWatch interation with Slack
 goal: Ec2 Instance --> CPU utilization > 80%(CloudWatch Metrics) --> SNS --> Lambda --> Slack

 sloution:- 1. store SlackWebHookURL in AWS System Manager by creating Parameter
            2. configure CloudWatch Metrics for the EC2 Instance
            3. create sns topic for the alaram ⏰ for notification
            4. create the lambda function 
            5. create a role with following permission and attach to lambda function
                 >AMAZONSSMFULLACCESS
                 >AWSLambdaBasicExecutionRole
                 >kms_policy_for_decryption
                   {
                      "Version":"2012-10-17",
                      "Statement": [
                              {
                                 "Effect":"Allow",
                                 "Action":[
                                      "kms":"Decrypt"    
                                 ],
                                 "Resource":[
                                      "arn:aws:kms:us-west-2:892515485494:key/b2ef131d-63d9-4fe2-8c99-193033419c76"
                                 ]    
                              }                      
                      ]
                    }
            6. now create the trigger by selceting SNS and associated topic to lambda function    
'''

import boto3
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

ssm=boto3.client('ssm') #Amazon Simple Systems Manager(ssm); Inside paramete store we have sotred our slack_webhook url
def lambda_handler(event,context):
     print(json.dumps(event)) # here event will be the sns for the cloudwatch alaram

     message=json.loads(event['Records'][0]['Sns']['Message'])
     print(json.dumps(message))

     alaram_name=message['AlarmName']
     new_state=message['NewStateValue']
     reason=message['NewStateReason']

     slack_message= {
         'text': ':fire: %s state is now %s: %s' % (alaram_name, new_state, reason)
       }
     webhook_url=ssm.get_parameter(Name='slack_webhook_url', WithDecryption=True)

     req = Request(webhook_url['Parameter']['Value'], json.dumps(slack_message).encode('utf-8'))

     try:
        response=urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
     except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
     except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
        
